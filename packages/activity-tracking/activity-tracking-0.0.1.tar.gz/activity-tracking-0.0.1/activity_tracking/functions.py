import platform
import ctypes
import logging
import csv
import subprocess
import os

logger = logging.getLogger()
"""This library inherits the logger of the importing library"""

if platform.system() == "Windows":
    # ctypes handles the Windows-specific functions
    from ctypes import wintypes, windll, create_unicode_buffer, byref

class LASTINPUTINFO(ctypes.Structure):
    # Special class for storing lastinputinfo data from windows
    _fields_ = [("cbSize", ctypes.c_ulong), ("dwTime", ctypes.c_ulong)]

def getForegroundWindow(userOS=platform.system()):
    # Get window name of current foreground window
    # RETURNS: str name of window

    window, _ = getForegroundWindow(userOS)
    return window

def getForegroundWindowProcess(userOS=platform.system()):
    """ Get window name and process name of current foreground window
     Makes use of windows API
     RETURNS: [str name of window, str name of process]
    """
    if userOS == "Windows":
        # Get the unique window ID of the foreground window
        windowId = windll.user32.GetForegroundWindow()

        # get title length of the window id (windowId)
        titleLength = windll.user32.GetWindowTextLengthW(windowId)

        # Create a buffer to put the title on
        # titleLength + 1 because C strings require an additional character
        # '\0' to terminate strings, I assume
        titleBuffer = create_unicode_buffer(titleLength + 1)

        # Get window text of the given window ID (windowId), store it to the
        # second argument (titleBuffer), and use 3rd arg as max length of text incl '\0'.
        windll.user32.GetWindowTextW(windowId, titleBuffer, titleLength + 1)

        # creates a dword type variable which will store the Process ID of the
        # foreground window
        pid = wintypes.DWORD()

        # Get process id of the given window ID (arg 1) and store it to
        # pid variable
        windll.user32.GetWindowThreadProcessId(windowId, byref(pid))

        # Run command 'tasklist', lookup which program has the pid
        # and store CSV output to var
        # TODO: try psutil?
        tasklist = os.popen(
            f'tasklist /FI \
						"pid eq {pid.value}" /FO CSV'
        )

        processNameCSV = tasklist.read()
        tasklist.close()

        # Returns a csv reader object
        readCSV = csv.reader(processNameCSV)
        listCSV = list(readCSV)

        # Position of the program name in the list
        # I wouldn't consider this portable so this might change.
        exeName = listCSV[10][0]

        # Return the window name, & process name running the window.
        return titleBuffer.value, exeName

    if userOS == "Linux":
        result = subprocess.run(
            ["timeout", "1", "xdotool", "getwindowfocus", "getwindowpid"],
            capture_output=True,
            text=True,
        )

        # pid is blank if no window is focused.
        if result.stdout == "":
            return "", ""

        proc = int(result.stdout)

        result = subprocess.run(
            ["timeout", "1", "ps", "-p", str(proc), "-o", "comm="],
            capture_output=True,
            text=True,
        )
        processName = result.stdout.strip("\n")

        result = subprocess.run(
            ["timeout", "1", "xdotool", "getwindowfocus", "getwindowname"],
            capture_output=True,
            text=True,
        )

        windowName = result.stdout.strip("\n")
        return windowName, processName

    logger.error("OS is Unknown: %s", userOS)
    raise Exception("OS is Unknown: %s", userOS)

def isUserActive(userOS=platform.system(), minGap=800):
    """
    Compares gap between last time of input from mouse or kb and current time.
    ARGS:
    	lastInputInfo -> Instance of class LASTINPUTINFO(ctypes.Structure),
    	minGap -> Int, minimum time between activity in mseconds
    	userOS -> string, the platform the user is using ["Windows", "Linux"]
    Returns:
      True if the user made an input during `minGap`, else False
    """

    ### TODO: Fix minGap linux implementation.

    # Store last input time to class
    if userOS == "Windows":

        lastInputInfo = LASTINPUTINFO()
        lastInputInfo.cbSize = ctypes.sizeof(LASTINPUTINFO)

        windll.user32.GetLastInputInfo(byref(lastInputInfo))
        lastInputTime = lastInputInfo.dwTime

        currentTime = windll.kernel32.GetTickCount()

        timeGap = currentTime - lastInputTime

        return timeGap <= minGap

    if userOS == "Linux":
        # Returns: 234324.2 234234.3
        # See proc man page for /proc/uptime
        # result = subprocess.run(["cat", "/proc/uptime"], capture_output=True, text=True)
        # Get first item only
        # currentTimeMs = float(result.stdout.split(" ")[0]) * 1000

        result = subprocess.run(
            # Implementation depends on this command:
            # timeout .1 xinput test-xi2 --root
            # If an input is made, EVENT is present.
            # timeout should be < mingap
            ["timeout", str((minGap / 1000) / 2), "xinput", "test-xi2", "--root"],
            capture_output=True,
            text=True,
        )
        # print( "EVENT" in result.stdout)
        return "EVENT" in result.stdout

    logger.error("OS is Unknown: %s")
    raise Exception("OS is Unknown: %s", userOS)

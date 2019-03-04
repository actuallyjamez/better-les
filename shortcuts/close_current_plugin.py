"""
Not currently possible due to the fact that I have no clue what im doing.
"""
import sys

# from AppKit import NSWorkspace

# if sys.platform == "darwin":
#     from AppKit import NSWorkspace
#     from Quartz import (
#         CGWindowListCopyWindowInfo,
#         kCGWindowListOptionOnScreenOnly,
#         kCGNullWindowID
#     )

#
# def close_current_plugin(keyboard):
#     # keyboard.press('f')
#
#     # active_app_name = NSWorkspace.sharedWorkspace().frontmostApplication().localizedName()
#     # print(active_app_name)
#     # !/usr/bin/python
#     # Prints list of windows in the current workspace.
#     if sys.platform == "darwin":
#         curr_app = NSWorkspace.sharedWorkspace().frontmostApplication()
#         curr_pid = NSWorkspace.sharedWorkspace().activeApplication()['NSApplicationProcessIdentifier']
#         curr_app_name = curr_app.localizedName()
#         options = kCGWindowListOptionOnScreenOnly
#         windowList = CGWindowListCopyWindowInfo(options, kCGNullWindowID)
#         for window in windowList:
#
#             pid = window['kCGWindowOwnerPID']
#             windowNumber = window['kCGWindowNumber']
#             ownerName = window['kCGWindowOwnerName']
#             geometry = window['kCGWindowBounds']
#             windowTitle = window.get('kCGWindowName', u'Unknown')
#             if curr_pid == pid:
#                 print(windowTitle)
#                 print("%s - %s (PID: %d, WID: %d): %s" % (
#                     ownerName, windowTitle, pid, windowNumber, geometry))
#     elif sys.platform == "win32":
#         (active_app_name, windowTitle) = _getActiveInfo_Win32()

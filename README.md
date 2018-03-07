# Keypirinha Plugin: ShareX

This is ShareX, a plugin for the
[Keypirinha](http://keypirinha.com) launcher.

This package allows you to execute ShareX actions and custom workflows.

## Download

https://github.com/Fuhrmann/keypirinha-sharex/releases


## Install

Once the `ShareX.keypirinha-package` file is installed,
move it to the `InstalledPackage` folder located at:

* `Keypirinha\portable\Profile\InstalledPackages` in **Portable mode**
* **Or** `%APPDATA%\Keypirinha\InstalledPackages` in **Installed mode** (the
  final path would look like
  `C:\Users\%USERNAME%\AppData\Roaming\Keypirinha\InstalledPackages`)


## Usage

Open Keypirinha and type 'ShareX'. Once the suggestion appears press ENTER to open ShareX or TAB to show all the actions you can execute.

## Configuration

This plugin uses the default ShareX folders to find the executable file and config files. If your installation/config files is in another path, please change it in the plugin configuration file.

The defaults are:
Path to exe: C:\Program Files\ShareX
Path to user config: C:\Users\YOUR_USER\Documents\ShareX

## Actions
<table>
    <tbody>
    <tr>
        <td>
            <div class="td_head">Action</div>
        </td>
        <td>
            <div class="td_head">Description</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_even">
            <div class="td_row_even">Upload file</div>
        </td>
        <td class="td_row_even">
            <div class="td_row_even">Select a file from your computer and upload</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_odd">
            <div class="td_row_odd">Upload folder</div>
        </td>
        <td class="td_row_odd">
            <div class="td_row_odd">Select a folder from your computer and upload</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_even">
            <div class="td_row_even">Upload from clipboard</div>
        </td>
        <td class="td_row_even">
            <div class="td_row_even">Upload the contents of your clipboard</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_odd">
            <div class="td_row_odd">Upload from clipboard with content viewer</div>
        </td>
        <td class="td_row_odd">
            <div class="td_row_odd">Upload the contents of your clipboard with content viewer</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_even">
            <div class="td_row_even">Upload text</div>
        </td>
        <td class="td_row_even">
            <div class="td_row_even">Specify a text and upload</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_odd">
            <div class="td_row_odd">Upload URL</div>
        </td>
        <td class="td_row_odd">
            <div class="td_row_odd">Specify an URL and upload</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_even">
            <div class="td_row_even">Drag and drop upload</div>
        </td>
        <td class="td_row_even">
            <div class="td_row_even">Upload a file using drag and drog</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_odd">
            <div class="td_row_odd">Shorten URL</div>
        </td>
        <td class="td_row_odd">
            <div class="td_row_odd">Specify an URL to shorten</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_even">
            <div class="td_row_even">Stop uploads</div>
        </td>
        <td class="td_row_even">
            <div class="td_row_even">Stop all current uploads</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_odd">
            <div class="td_row_odd">Capture screen</div>
        </td>
        <td class="td_row_odd">
            <div class="td_row_odd">Take a screenshot of the current screen</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_even">
            <div class="td_row_even">Capture active window</div>
        </td>
        <td class="td_row_even">
            <div class="td_row_even">Take a screenshot of the active window</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_odd">
            <div class="td_row_odd">Capture active monitor</div>
        </td>
        <td class="td_row_odd">
            <div class="td_row_odd">Take a screenshot of the active monitor</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_even">
            <div class="td_row_even">Capture rectangle region</div>
        </td>
        <td class="td_row_even">
            <div class="td_row_even">Take a screenshot of a rectangle user selected region</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_odd">
            <div class="td_row_odd">Capture rectangle light</div>
        </td>
        <td class="td_row_odd">
            <div class="td_row_odd">Take a screenshot of a rectangle user selected region (less gui)</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_even">
            <div class="td_row_even">Capture rectangle transparent</div>
        </td>
        <td class="td_row_even">
            <div class="td_row_even">Take a screenshot of a rectangle user selected region (without gui)</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_odd">
            <div class="td_row_odd">Capture last region</div>
        </td>
        <td class="td_row_odd">
            <div class="td_row_odd">Take a screenshot of the last user selected region</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_even">
            <div class="td_row_even">Scrolling capture</div>
        </td>
        <td class="td_row_even">
            <div class="td_row_even">Take a screenshot using scrolling region</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_odd">
            <div class="td_row_odd">Capture webpage</div>
        </td>
        <td class="td_row_odd">
            <div class="td_row_odd">Specify a webpage to screenshot</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_even">
            <div class="td_row_even">Text capture</div>
        </td>
        <td class="td_row_even">
            <div class="td_row_even">Specify a region to capture and transform to text (OCR)</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_odd">
            <div class="td_row_odd">Auto capture</div>
        </td>
        <td class="td_row_odd">
            <div class="td_row_odd">Take one or more screenshots using a timer</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_even">
            <div class="td_row_even">Record screen</div>
        </td>
        <td class="td_row_even">
            <div class="td_row_even">Record the current screen</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_odd">
            <div class="td_row_odd">Record active window</div>
        </td>
        <td class="td_row_odd">
            <div class="td_row_odd">Record the active window</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_even">
            <div class="td_row_even">Start screen recorder</div>
        </td>
        <td class="td_row_even">
            <div class="td_row_even">Start recording the screen with a predefined region</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_odd">
            <div class="td_row_odd">Record screen (GIF)</div>
        </td>
        <td class="td_row_odd">
            <div class="td_row_odd">Record the current screen (GIF)</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_even">
            <div class="td_row_even">Record screen window (GIF)</div>
        </td>
        <td class="td_row_even">
            <div class="td_row_even">Record the active window (GIF)</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_odd">
            <div class="td_row_odd">Start screen record (GIF)</div>
        </td>
        <td class="td_row_odd">
            <div class="td_row_odd">Start recording the screen (GIF) with a predefined region</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_even">
            <div class="td_row_even">Abort screen record</div>
        </td>
        <td class="td_row_even">
            <div class="td_row_even">Stop the screen recort</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_odd">
            <div class="td_row_odd">Color picker</div>
        </td>
        <td class="td_row_odd">
            <div class="td_row_odd">Open the color picker tool</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_even">
            <div class="td_row_even">Screen color picker</div>
        </td>
        <td class="td_row_even">
            <div class="td_row_even">Choose an element in the screen to copy its color</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_odd">
            <div class="td_row_odd">Image editor</div>
        </td>
        <td class="td_row_odd">
            <div class="td_row_odd">Open the default image editor</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_even">
            <div class="td_row_even">Image effects</div>
        </td>
        <td class="td_row_even">
            <div class="td_row_even">Apply effects to an image</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_odd">
            <div class="td_row_odd">Hash check</div>
        </td>
        <td class="td_row_odd">
            <div class="td_row_odd">Check the hash of a file</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_even">
            <div class="td_row_even">DNS changer</div>
        </td>
        <td class="td_row_even">
            <div class="td_row_even">Open the DNS changer tool</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_odd">
            <div class="td_row_odd">QRCode</div>
        </td>
        <td class="td_row_odd">
            <div class="td_row_odd">Encode or decode a qrcode</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_even">
            <div class="td_row_even">Ruler</div>
        </td>
        <td class="td_row_even">
            <div class="td_row_even">Open the ruler tool</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_odd">
            <div class="td_row_odd">Image combiner</div>
        </td>
        <td class="td_row_odd">
            <div class="td_row_odd">Combine two or more images into one</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_even">
            <div class="td_row_even">Video thumbnailer</div>
        </td>
        <td class="td_row_even">
            <div class="td_row_even">Create thumbanils for videos</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_odd">
            <div class="td_row_odd">FTP client</div>
        </td>
        <td class="td_row_odd">
            <div class="td_row_odd">Open the FTP client</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_even">
            <div class="td_row_even">Tweet message</div>
        </td>
        <td class="td_row_even">
            <div class="td_row_even">Tweet a message using a predefined twitter account</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_odd">
            <div class="td_row_odd">Monitor test</div>
        </td>
        <td class="td_row_odd">
            <div class="td_row_odd">Run the moninor test</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_even">
            <div class="td_row_even">Disable hotkeys</div>
        </td>
        <td class="td_row_even">
            <div class="td_row_even">Disable all hotkeys</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_odd">
            <div class="td_row_odd">Open main window</div>
        </td>
        <td class="td_row_odd">
            <div class="td_row_odd">Open the main ShareX window</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_even">
            <div class="td_row_even">Open screenshots folder</div>
        </td>
        <td class="td_row_even">
            <div class="td_row_even">Open the default screenshots folder</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_odd">
            <div class="td_row_odd">Open history</div>
        </td>
        <td class="td_row_odd">
            <div class="td_row_odd">Open the history window</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_even">
            <div class="td_row_even">Open image history</div>
        </td>
        <td class="td_row_even">
            <div class="td_row_even">Open the image history window</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_odd">
            <div class="td_row_odd">Toogle actions toolbar</div>
        </td>
        <td class="td_row_odd">
            <div class="td_row_odd">Show/hide the actions toolbar</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_even">
            <div class="td_row_even">Exit ShareX</div>
        </td>
        <td class="td_row_even">
            <div class="td_row_even">Close ShareX</div>
        </td>
    </tr>
    <tr>
        <td class="td_row_odd">
            <div class="td_row_odd">Custom workflow</div>
        </td>
        <td class="td_row_odd">
            <div class="td_row_odd">Press TAB to list your custom workflows</div>
        </td>
    </tr>
    </tbody>
</table>

## Custom workflows

To execute your customized workflows select "Custom workflow" action, press TAB and all your workflows will be listed. Select one and press ENTER to execute.

## Change Log

### v1.0

* Released


## License

This package is distributed under the terms of the MIT license.
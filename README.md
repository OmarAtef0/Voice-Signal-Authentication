# Voice-Signal-Authentication
<p>This desktop app utilizes concepts of fingerprinting and spectrograms to recognize authorized individuals and grant access accordingly. It operates in two modes: Security Voice Code and Security Voice Fingerprint.</p>

<h2>Features</h2>
<h3>Mode 1: Security Voice Code</h3>
<p>In this mode, access is granted only if the spoken voice matches one of the predefined pass-code sentences. The following sentences are considered valid passcodes:</p>
<ol>
  <li>"Open middle door"</li>
  <li>"Unlock the gate"</li>
  <li>"Grant me access"</li>
</ol>
<p>Users can choose alternative passcode sentences as long as they do not contain similar words among the three chosen sentences.</p>

<h3>Mode 2: Security Voice Fingerprint</h3>
<p>Access is granted to specific individuals who say the valid pass-code sentence. Users can select which individual(s) out of the original 8 users are granted access through the settings UI. Access can be granted to one or more individuals.</p>

<h2>User Interface (UI)</h2>
<p>The UI provides the following elements:</p>
<ul>
  <li>Button to Start Recording: Initiates the recording of the voice-code.</li>
  <li>Spectrogram Viewer: Displays the spectrogram of the spoken voice-code.</li>
  <li>Summary for Analysis Results:
      <ol>
          <li>Table indicating how much the spoken sentence matches each of the saved three passcode sentences.</li>
          <li>Table indicating how much the spoken voice matches each of the 8 saved individuals.</li>
      </ol>
  </li>
  <li>Result Indicator: UI element indicating whether the algorithm results in "Access gained" or "Access denied".</li>
</ul>

<h2>Usage</h2>
<ol>
  <li>Clone this repository to your local machine.</li>
  <li>Open the project in your preferred IDE.</li>
  <li>Run the application.</li>
  <li>Use the provided UI to interact with the software, select operation mode, record voice-code, and view analysis results.</li>
</ol>

<h2>Contributions</h2>
<p>Contributions to this project are welcome. If you find any issues or have suggestions for improvements, please feel free to submit a pull request or open an issue on GitHub.</p>

<h2>License</h2>
<p>This project is licensed under the <a href="LICENSE">MIT License</a>. Feel free to use, modify, and distribute this software according to the terms of the license.</p>

## Contributors

We would like to acknowledge the following individuals for their contributions:

<table>
  <tr>
    <td align="center">
      <a href="https://github.com/OmarAtef0" target="_black">
      <img src="https://avatars.githubusercontent.com/u/131784941?v=4" width="150px;" alt="Omar Atef"/>
      <br />
      <sub><b>Omar Atef</b></sub></a>
    </td>  
    <td align="center">
      <a href="https://github.com/IbrahimEmad11" target="_black">
      <img src="https://avatars.githubusercontent.com/u/110200613?v=4" width="150px;" alt="Omar Atef"/>
      <br />
      <sub><b>Ibrahim Emad</b></sub></a>
    </td>  
    <td align="center">
      <a href="https://github.com/Hazem-Raafat" target="_black">
      <img src="https://avatars.githubusercontent.com/u/100636693?v=4" width="150px;" alt="Omar Atef"/>
      <br />
      <sub><b>Hazem Rafaat</b></sub></a>
    </td>  
    <td align="center">
      <a href="https://github.com/Ahmedkhaled222" target="_black">
      <img src="https://avatars.githubusercontent.com/u/109425772?v=4" width="150px;" alt="Omar Atef"/>
      <br />
      <sub><b>Ahmed Khaled</b></sub></a>
    </td>  
  </tr>
 </table>
  

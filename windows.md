# Windows

## Install
Tested using Python 3.13.13, pip 26.0.1
```
git clone https://github.com/jglane/cyclemetry.git
cd cyclemetry
python -m venv venv
./venv/Scripts/activate
pip install -r requirements.txt
```
* Install [ffmpeg](https://ffmpeg.org/)
* Add gpx file to root directory

## Edit the template
Necessary changes
* Under course, change "width" and "height" to match the aspect ratio of your course map
* Under scene, change "start" and "end" to the timestamps in seconds you want the overlay to cover in the gpx file

## Render the overlay
Demo a frame first to check the template
```
python main.py <gpx_file> <template_filename> demo
```
When that looks good, start rendering the overlay
```
python main.py <gpx_file> <template_filename>
```

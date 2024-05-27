# wuwa-fps-unlocker (USE AT YOUR OWN RISK!!!!!! )

A simple python script to uncap Wuthering Waves' Framerate

Credit to [Dim on Twitter](https://x.com/Notmdi/status/1793581051765473508) for finding this one out

# Requirements

For building an executable and running as a command, only [Python](https://python.org) is required.

# Using

## Using pre-built executables

You can find pre-built executables in the latest build action under any passing [build artifacts](https://github.com/calicokatsu/wuwa-fps-unlocker/actions/workflows/build.yaml) or under [Releases](https://github.com/calicokatsu/wuwa-fps-unlocker/releases)

## Building an Executable

First, clone the repository and enter it's directory

```sh
git clone https://github.com/calicokatsu/wuwa-fps-unlocker
cd wuwa-fps-unlocker
```

#### Using pyinstaller

you can install pick and pyinstaller using requirements.txt using the following commands

```sh
pip install -r requirements
```

or you can install them both manually. The rest of the libraries used in this script are built into python.

```sh
pip install pick
pip install pyinstaller
```

**or**

```sh
python -m pip install pick
python -m pip install pyinstaller
```

Then, Simply run the following commands:

```sh
pyinstaller -F main.py
```

and voila, you should now have the script bundled into an exe in the newly created `dist` folder. Run the executable as administrator, follow the instructions and enjoy (gl on your pulls <3)

## Running as a standard python script

Run the following command with an elevated command prompt, follow the instructions and enjoy

```sh
python main.py
```

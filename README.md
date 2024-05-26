A simple python script to uncap Wuthering Waves' 60 FPS Framerate Cap

I am not sure who came up with the original idea to edit LocalStorage but if anyone knows, open a PR with an edit please and thanks

# Using

## Cloning the Repository

```sh
git clone https://github.com/calicokatsu/wuwa-fps-unlocker
```

## Building an Executable

#### Using pyinstaller

you can install pick and pyinstaller using requirements.txt using the following commands

```sh
pip install -r requirements
```

or you can install them both manually. The rest of the libraries used in this script are built in.

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

and voila, you should now have the script bundled into an exe in the newly created `dist` folder.

## Running as a standard python script

Run the following command

```sh
python main.py
```

simple & clean

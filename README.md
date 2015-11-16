# Fun with TensorFlow

Don't use the binary package; it's behind the source and lacks the functionality to run anything but the most basic examples.

## Install from Source

This is a modified version of the instructions from https://github.com/tensorflow/tensorflow<br>
This is what worked for me as of 14-Nov 2015.

### The following instructions are for Mac OS X.

Prerequisites:

[Install XCode 6.1 or later.](https://developer.apple.com/xcode/downloads/)<br>
[Install JDK 8](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)

### Download the Bazel installer script

Download [bazel-0.1.1-installer-darwin-x86_64.sh](https://github.com/bazelbuild/bazel/releases)

Run it:
```
$ chmod +x bazel-0.1.1-installer-darwin-x86_64.sh
$ ./bazel-0.1.1-installer-darwin-x86_64.sh --user
```

Add Bazel to $PATH:
```
$ export PATH="$PATH:$HOME/bin"
```
Also add that line to ~/.bash_profile

### Download PCRE

Download pcre-8.37.tar.gz here:
```
ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/
```
Run, install.

### Download SWIG

Download [swig-3.0.7.tar.gz](http://sourceforge.net/projects/swig/files/swig/swig-3.0.7/)

In the same directory, run the following commands:

```
$ ./configure
$ make
$ make install
```

Check to see if the install worked. The tests take a long time; you may want to ^C and kill it after a couple minutes.

```
$ make -k check
```

### Install numpy

```
$ pip install numpy
```
Get [Anaconda](https://www.continuum.io/downloads) if numpy doesn't work.

### Get the tensorflow source
```
$ git clone --recurse-submodules https://github.com/tensorflow/tensorflow
```

### Create the pip package and install

```
$ bazel build -c opt //tensorflow/tools/pip_package:build_pip_package

$ bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg

$ pip install /tmp/tensorflow_pkg/tensorflow-0.5.0-py2-none-any.whl
```

### Build the models

```
$ cd tensorflow/tensorflow/models
$ bazel build 
```

Okay, finally done!

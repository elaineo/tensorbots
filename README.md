# Fun with TensorFlow

Don't use the binary package; it's behind the source and lacks the functionality to run anything but the most basic examples.

## Install from Source

This is a modified version of the instructions from https://github.com/tensorflow/tensorflow
Their instructions were incomplete as of 14-Nov 2015.

### The following instructions are for Mac OS X.

```
$ git clone --recurse-submodules https://github.com/tensorflow/tensorflow
```

[Install XCode 6.1 or later.](https://developer.apple.com/xcode/downloads/)<br>
[Install JDK 8](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)

### Download the Bazel installer script

[bazel-0.1.1-installer-darwin-x86_64.sh ](https://github.com/bazelbuild/bazel/releases/download/0.1.1/bazel-0.1.1-installer-darwin-x86_64.sh)

Run it:
```
$ chmod +x bazel-0.1.1-installer-darwin-x86_64.sh
$ ./bazel-0.1.1-installer-darwin-x86_64.sh --user
```

Add Bazel to $PATH:
```
$ export PATH="$PATH:$HOME/bin"
```
Also add that to ~/.bash_profile

### Download PCRE

[pcre-8.37.tar.gz](ftp://ftp.csx.cam.ac.uk/pub/software/programming/pcre/pcre-8.37.tar.gz)

Run, install.

### Download SWIG

[swig-3.0.7.tar.gz](http://prdownloads.sourceforge.net/swig/swig-3.0.7.tar.gz)

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

### Create the pip package and install

```
$ bazel build -c opt //tensorflow/tools/pip_package:build_pip_package

$ bazel-bin/tensorflow/tools/pip_package/build_pip_package /tmp/tensorflow_pkg

$ pip install /tmp/tensorflow_pkg/tensorflow-0.5.0-py2-none-any.whl
```

Okay, finally done!

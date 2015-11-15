# Fun with TensorFlow

Don't use the binary package; it's behind the source and lacks the functionality to run anything but the most basic examples.

## Install from Source

This is a modified version of the instructions from https://github.com/tensorflow/tensorflow
Their instructions didn't work as of 14-Nov 2015.

<b>The following instructions are for Mac OS X. </b>

'''
$ git clone --recurse-submodules https://github.com/tensorflow/tensorflow
'''

[Install XCode 6.1 or later.](https://developer.apple.com/xcode/downloads/)<br>
[Install JDK 8](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html)

Download the Bazel installer script: [bazel-0.1.1-installer-darwin-x86_64.sh ](https://github.com/bazelbuild/bazel/releases/download/0.1.1/bazel-0.1.1-installer-darwin-x86_64.sh)


Run it:
'''
$ chmod +x bazel-0.1.1-installer-darwin-x86_64.sh
$ ./bazel-0.1.1-installer-darwin-x86_64.sh --user
'''


# KBIR - Keyboard Intermediate Representation 
[![Build Status](https://travis-ci.org/rswiernik/KBIR.svg?branch=master)](https://travis-ci.org/rswiernik/KBIR)

*Please be aware that this project is under heavy development and is not stable or recommended for use. The build status, while representative of tests being run, tests are not ensured to be wholey inclusive of any features.*

KBIR is a project that aims to make the process of creating layouts for your keyboard a little easier.

## How it works

KBIR takes a very simple representation of your keyboard layout and translates it into a usable format with your firmware. This process happens as 2 distinct steps.

1. The layout file (.kbl) is interpreted into KBIR.
2. The KBIR is then translated down into the neccessary layout files for whatever firmware you are using.


py_binary(
    name = "kbir",
    srcs = ["source/kbirparse.py"],
    deps = [
        ":kbirlib",
    ],
    visibility = [
        "//project:__subpackages__",
    ],
    main = "source/kbirparse.py",
)

py_library(
    name = "kbirlib",
    srcs = ["source/kbirlib.py"],
)

py_test(
    name = "runtests",
    srcs = ["//tests:test_build"],
)

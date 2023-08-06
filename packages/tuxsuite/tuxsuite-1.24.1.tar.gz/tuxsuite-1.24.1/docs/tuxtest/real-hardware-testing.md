# Testing on Real hardware with TuxSuite

TuxSuite can now run user tests on Real Hardware using LAVA in the
backend. A build successfully completed in TuxBuild can be tested in a
real hardware in LAVA through TuxTest. This feature uses uses
[lava-test-plans](https://github.com/Linaro/lava-test-plans) in order
to submit a LAVA job to a LAVA instance.

## Options

There are two important options used when submitting a test using the
TuxSuite cli on real hardware.

### lab

The lab option is used to select the LAVA instance to which the test
should be submitted.

```shell
tuxsuite test --device x15 \
    --lab https://lkft.validation.linaro.org \
    --kernel https://storage.tuxsuite.com/public/linaro/lkft/builds/2SzdP2Y00UvIcS3f56EaTILWuLX/zImage \
    --modules https://storage.tuxsuite.com/public/linaro/lkft/builds/2SzdP2Y00UvIcS3f56EaTILWuLX/modules.tar.xz \
    --rootfs https://storage.tuxboot.com/debian/20230714/bookworm/armhf/rootfs.ext4.xz \
    --dtb https://storage.tuxsuite.com/public/linaro/lkft/builds/2SzdP2Y00UvIcS3f56EaTILWuLX/dtbs/am57xx-beagle-x15.dtb \
    --parameters DEPLOY_OS=debian
```

This value can also be set in the tuxsuite config file
`~/.config/tuxsuite/config.ini` as follows:

`lab = https://lkft.validation.linaro.org`

It can also be supplied as an environment variable which is shown as
follows:

`export TUXSUITE_LAB=https://lkft.validation.linaro.org`

__note__: The default LAVA lab instance is
<https://lkft.validation.linaro.org>

### lava-test-plans-project

The lava-test-plans-project option is used to choose the
lava-test-plans project.

```shell
tuxsuite test --device x15 \
    --lava-test-plans-project lkft \
    --kernel https://storage.tuxsuite.com/public/linaro/lkft/builds/2SzdP2Y00UvIcS3f56EaTILWuLX/zImage \
    --modules https://storage.tuxsuite.com/public/linaro/lkft/builds/2SzdP2Y00UvIcS3f56EaTILWuLX/modules.tar.xz \
    --rootfs https://storage.tuxboot.com/debian/20230714/bookworm/armhf/rootfs.ext4.xz \
    --dtb https://storage.tuxsuite.com/public/linaro/lkft/builds/2SzdP2Y00UvIcS3f56EaTILWuLX/dtbs/am57xx-beagle-x15.dtb \
    --parameters DEPLOY_OS=debian
```

This value can also be set in the tuxsuite config file
`~/.config/tuxsuite/config.ini` as follows:

`lava_test_plans_project = lkft`

It can also be supplied as an environment variable which is shown as
follows:

`export TUXSUITE_LAVA_TEST_PLANS_PROJECT=lkft`

__note__: The default lava-test-plans-project is `None`

## Plan with build and boot test

!!! info "A sample plan"
    <details>
    <summary>Click to see the plan contents</summary>

    ```
    lkftfragments: &lkftfragments
      - &frag-lkft-base https://raw.githubusercontent.com/Linaro/meta-lkft/kirkstone/meta/recipes-kernel/linux/files/lkft.config
      - &frag-lkft-crypto https://raw.githubusercontent.com/Linaro/meta-lkft/kirkstone/meta/recipes-kernel/linux/files/lkft-crypto.config
      - &frag-lkft-distro https://raw.githubusercontent.com/Linaro/meta-lkft/kirkstone/meta/recipes-kernel/linux/files/distro-overrides.config
      - &frag-lkft-systemd https://raw.githubusercontent.com/Linaro/meta-lkft/kirkstone/meta/recipes-kernel/linux/files/systemd.config
      - &frag-lkft-virtio https://raw.githubusercontent.com/Linaro/meta-lkft/kirkstone/meta/recipes-kernel/linux/files/virtio.config

    version: 1
    name: x15 build and boot test.
    description: Demonstrate a build and boot test with x15 via real hardware
    jobs:
    - name: arm-lkftconfig-dut
      builds:
        - build_name: gcc-10-lkftconfig
          target_arch: arm
          toolchain: gcc-10
          kconfig: [ defconfig, *frag-lkft-base, *frag-lkft-crypto, *frag-lkft-distro, *frag-lkft-systemd, *frag-lkft-virtio, CONFIG_ARM_TI_CPUFREQ=y, CONFIG_SERIAL_8250_OMAP=y, CONFIG_POSIX_MQUEUE=y, CONFIG_OF=y, CONFIG_SYN_COOKIES=y, CONFIG_SCHEDSTATS=y, CONFIG_AHCI_DWC=y, CONFIG_KFENCE=n ]
      tests:
        - device: x15
          boot_args: rw
          parameters: {DEPLOY_OS: "debian"}
          dtb: am57xx-beagle-x15.dtb
          rootfs: https://storage.tuxboot.com/debian/20230714/bookworm/armhf/rootfs.ext4.xz
    ```

    </details>

Submitting the above plan file will build the kernel and submit the
test as a LAVA job with the kernel build artifacts.

```shell
tuxsuite plan submit \
    --git-repo https://gitlab.com/Linaro/lkft/mirrors/torvalds/linux-mainline \
    --git-ref master \
    --lab https://validation.linaro.org/ \
    --lava-test-plans-project lkft \
    x15-boot-plan.yaml
```

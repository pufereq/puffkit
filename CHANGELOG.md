# Changelog

All notable changes to this project will be documented in this file.

## [0.4.0] - 2024-10-29

### Features

- [`23a8aed`](https://github.com/pufereq/template-repo/commit/23a8aede748a28f3718df3229232854a81fb7fad) **app.py**: add fallback scene, set by default
- [`22f2253`](https://github.com/pufereq/template-repo/commit/22f2253d12fc8e3fb649856f96f4ad69ff56eb01) **scene.py**: add `_id` argument to `PkScene's` `__init__` instead of assigning id based on class name

### Miscellaneous Tasks

- [`78da30d`](https://github.com/pufereq/template-repo/commit/78da30dd2e82eddcfa2e2d6000cc5a57bc7b918d) **scene.py**: use `default` font from `app` instead of monospace
- [`c0ed583`](https://github.com/pufereq/template-repo/commit/c0ed58344f24b0288111a98a16619f35e273bf6a) **scene.py**: draw 'fallback scene' text only when id is `fallback` instead of type
- [`4364c16`](https://github.com/pufereq/template-repo/commit/4364c16590bee511d47ff80d87eebd516e857829) **app.py**: import `PkScene` in module
- [`6c64108`](https://github.com/pufereq/template-repo/commit/6c641081cff7c6bea0cefcfe52d17077e92c7f94) **scene.py**: require keyword argument `lazy` in `PkScene.__init__()`

### Testing

- [`e79b351`](https://github.com/pufereq/template-repo/commit/e79b351374b272606804ddf387f337fb97d62bd0) **test_scene.py**: modify tests to provide new arguments to `PkScene`

## [0.3.0] - 2024-10-27

### Bug Fixes

- [`4425bb9`](https://github.com/pufereq/template-repo/commit/4425bb987323a57c85d04c5d3bb903463b0a95a2) **app.py**: fix wrong placement of `None ` type in `PkApp.add_font()` method

### Features

- [`938fb14`](https://github.com/pufereq/template-repo/commit/938fb14c3bb21d9d1a73c6e73befaeeec9aa1174) **app.py**: rename `PkApp.change_scene()` -> `set_scene()`
- [`4edb011`](https://github.com/pufereq/template-repo/commit/4edb01171a7d0b1c65895c3a18c0bffbcbcad52e) **app.py**: add support for scene lazy-loading in `PkApp.set_scene()`
- [`02a4544`](https://github.com/pufereq/template-repo/commit/02a4544aeb79ce4469cf732315790a92d70146a3) **scene.py**: add lazy scene-loading

### Miscellaneous Tasks

- [`a9391a7`](https://github.com/pufereq/template-repo/commit/a9391a75ea7a57a81a8d902fae35d8efe392f919) **app.py**: add log calls to several methods for verbosity
- [`24335b0`](https://github.com/pufereq/template-repo/commit/24335b0834c507f54cd076f48b3c4f0ba95264bc) **app.py**: modify `size` argument of call to `PkSurface` (`PkApp.internal_screen_surface`)
- [`dafbe29`](https://github.com/pufereq/template-repo/commit/dafbe2923d3724775b40995373e7d8bf0f69a9c5) **scene.py**: alter type of `self.pos` and `self.size` to adhere to PkSurface's new types
- [`0b1c18d`](https://github.com/pufereq/template-repo/commit/0b1c18d00ef5319bfb09efadbc3e1847eb2bb741) **surface.py**: use only `PkSize` and `PkCoordinate` for initializing geometry

### Styling

- [`5be3709`](https://github.com/pufereq/template-repo/commit/5be37091accc009697da804d54984b75387c17b1) **app.py**: add type checking-only imports
- [`3a15bb7`](https://github.com/pufereq/template-repo/commit/3a15bb7b7c723e960b7683c9d9bb784366c8721b) **scene.py**: add type checking-only imports
- [`47e145e`](https://github.com/pufereq/template-repo/commit/47e145eb774e2288f089fbad44460ab301adeb22) **surface.py**: add type checking-only imports

### Testing

- [`b1f2746`](https://github.com/pufereq/template-repo/commit/b1f2746bd8fc3cf9c0b6cca2aabbeacf25c95488) **test_app.py**: add tests for new conditions in `PkApp.set_scene()`
- [`1a01496`](https://github.com/pufereq/template-repo/commit/1a01496a08c4eb03fda83ad6754e29fd5f5dc102) **test_app.py**: modify tests to adhere to PkApp's changes
- [`53393cd`](https://github.com/pufereq/template-repo/commit/53393cd47aa5eda3d9ce7e328053f513a86ad13f) **test_app.py**: add test for TYPE_CHECKING conditional
- [`9dd1ddd`](https://github.com/pufereq/template-repo/commit/9dd1dddeb95a567b4a712dd9b434e700d60c54c4) **test_scene.py**: add test for TYPE_CHECKING conditional
- [`90f5166`](https://github.com/pufereq/template-repo/commit/90f516616e89d94e23a13706776bddd93fd3b146) **test_surface.py**: add test for TYPE_CHECKING conditional

## [0.2.1] - 2024-09-30

### Bug Fixes

- [`fe680d0`](https://github.com/pufereq/template-repo/commit/fe680d031ef7ebe65053590f4f0b8f44e420090c) **app.py**: fix circular import

### Miscellaneous Tasks

- [`e80d032`](https://github.com/pufereq/template-repo/commit/e80d0329c659f9d3facf21e695e528c4caef9dba) **scene.py**: use `PkApp` as argument instead of `size` and `pos`

### Revert

- [`1b3f84e`](https://github.com/pufereq/template-repo/commit/1b3f84ead76cbe20e7343e2ba8d0924099616140) **size.py**: bring back `width` and `height` properties

### Testing

- [`e999fab`](https://github.com/pufereq/template-repo/commit/e999fabcdc46908f9dc5f6fbf70fa02930a35df2) **test_scene.py**: adjust tests to argument changes
- [`ded3260`](https://github.com/pufereq/template-repo/commit/ded3260569d8078d45833b34ac29d3a03723b817) **test_size.py**: fix naming of functions

## [0.2.0] - 2024-09-30

### Documentation

- [`ae2f866`](https://github.com/pufereq/template-repo/commit/ae2f866d6340218e9ad6c33e6b41edc9d82f5603) **coordinate.py**: correct docstring to not include sizes

### Features

- [`35fef74`](https://github.com/pufereq/template-repo/commit/35fef7441b49e9e3b5cc1b03600e190529e03a7c) **size.py**: add support for floats
- [`d582781`](https://github.com/pufereq/template-repo/commit/d582781eefe07ac5c80f0afd1510910733b29b8a) **coordinate.py**: add support for floats
- [`313bc7c`](https://github.com/pufereq/template-repo/commit/313bc7c3565af8bdc40c6a2a2add05421c85e7ce) **size.py**: add `PkSize` class
- [`4f8b96b`](https://github.com/pufereq/template-repo/commit/4f8b96b38384b906137f167dda4cf16f2cc4df5b) **coordinate.py**: add `PkCoordinate` class

### Miscellaneous Tasks

- [`2127283`](https://github.com/pufereq/template-repo/commit/2127283f205d0b3a5f8758e399a98ac5bcdee30a) **surface.py**: use `PkSize` and `PkCoordinate` for geometry
- [`b35315a`](https://github.com/pufereq/template-repo/commit/b35315a0e0033c55f2854f7f86692b5e6bac9b26) **app.py**: use `PkSize` for sizes
- [`b8c90a4`](https://github.com/pufereq/template-repo/commit/b8c90a4cc1607359b7be73c1fa8324ce371743b4) **commit_checks.yaml**: make coverage report prettier
- [`9fa443c`](https://github.com/pufereq/template-repo/commit/9fa443c9054b44466dbdf3ebe9ecc8a41889b526) **commit_checks.yaml**: add coverage reports
- [`4a97393`](https://github.com/pufereq/template-repo/commit/4a973934fef117efdf6476e0391efe111ab907f0) **pr_checks.yaml**: add newline at end of file
- [`74e1733`](https://github.com/pufereq/template-repo/commit/74e1733263ce35e3b4032a3823bfba452895e84d) **pr_checks.yaml**: rename `test.yaml` to `commit_checks.yaml` for better readability
- [`a5424e8`](https://github.com/pufereq/template-repo/commit/a5424e882c43a6b3e09e628dc38fc8b91822d5e5) **pr_checks.yaml**: rename `coverage.yaml` to `pr_checks.yaml` for better readability
- [`4071b95`](https://github.com/pufereq/template-repo/commit/4071b95711a20232b62a6ea4374723f9da802828) **size.py**: add `PkSize.w` and `PkSize.h` aliases as `width` and `height`
- [`bc80992`](https://github.com/pufereq/template-repo/commit/bc80992ef31ec65265e7bbb7c6da683c97295093) **rect.py**: move module into `geometry/` subdirectory
- [`754e413`](https://github.com/pufereq/template-repo/commit/754e413b9cb37c2e1640e112e84283aa6261b5c4) **coordinate.py**: move module into `geometry/` subdirectory
- [`f9a409c`](https://github.com/pufereq/template-repo/commit/f9a409c0307d293a45ef7570ecf6e97273e755fc) **__init__.py**: add `PkCoordinate` import

### Revert

- [`abbaaa4`](https://github.com/pufereq/template-repo/commit/abbaaa4c1e63b7db73c6151795f36e9cd5f92a2f) **size.py**: revert "chore(size.py): add `PkSize.w` and `PkSize.h` aliases as `width` and `height`"

### Styling

- [`2fe7a92`](https://github.com/pufereq/template-repo/commit/2fe7a92a22128eca6c1b74d03b02883d9b9b7bd5) **size.py**: fix wrong type hints used in `__iter__` and `__getitem__` methods

### Testing

- [`5b02c0c`](https://github.com/pufereq/template-repo/commit/5b02c0c67d19a829b245e756bdcea9a33464cd3e) **test_size.py**: modify tests to also use tuples instead of always PkSizes
- [`53cf4f0`](https://github.com/pufereq/template-repo/commit/53cf4f03cedc4ece00680783d999e86064230251) **test_coordinate.py**: modify tests to also use tuples instead of always PkCoordinates
- [`e2e538d`](https://github.com/pufereq/template-repo/commit/e2e538d8d31569b8be0442c4db37abf2353a326a) **test_size.py**: add tests for `size.py` module
- [`a967ebc`](https://github.com/pufereq/template-repo/commit/a967ebc4b1ce26d56d828dac4ad9d504207a2237) **test_surface**: correct import of `PkRect` after rename
- [`5ec176b`](https://github.com/pufereq/template-repo/commit/5ec176b81200e62f89b097d7e273df4fcfbe5855) **test_rect.py**: move test module into `geometry/` subdirectory
- [`1fa95db`](https://github.com/pufereq/template-repo/commit/1fa95db0caedacb288bcf4ec8e365e8ae208a516) **test_coordinate.py**: add tests for `coordinate.py`

## [0.1.0] - 2024-09-28

### Documentation

- [`06a4242`](https://github.com/pufereq/template-repo/commit/06a424279cf6b7cdcff1bf60691f6cc5f10bd3b9) **README.md**: change capitalization of 'puffkit'

### Features

- [`d084052`](https://github.com/pufereq/template-repo/commit/d084052ff9f661dfaf29ee904b61547f3806ca2a) **app.py**: add `PkApp` class
- [`78b11a7`](https://github.com/pufereq/template-repo/commit/78b11a7674088f1ea4fc9555e8449436ca7d6967) **scene.py**: add `PkScene` class
- [`b9cfd51`](https://github.com/pufereq/template-repo/commit/b9cfd519ba862ede6085487f2fe61d7e528f9300) **textures.py**: add `get_texture()` function
- [`8cee2c6`](https://github.com/pufereq/template-repo/commit/8cee2c612c6867562035691f03c8e644e43a979e) **subsurface.py**: add `PkSubSurface` class
- [`2d05b32`](https://github.com/pufereq/template-repo/commit/2d05b32e563159aa79691a85269d6b3a7f275a8f) **surface.py**: add `PkSurface` class
- [`b66d526`](https://github.com/pufereq/template-repo/commit/b66d5261b1040df7473fa2672eff3dd6a006e682) **palettes.py**: add `PkBasicPalette` palette
- [`88ffbc3`](https://github.com/pufereq/template-repo/commit/88ffbc3a251cb9d652d914cabdd063fb9e4f8ed6) **sysfont.py**: add `PkSysFont` class
- [`e2b59da`](https://github.com/pufereq/template-repo/commit/e2b59dae463e728531aacf3a3a9d5b6d6fee1f08) **font.py**: add `PkFont` class
- [`68f244a`](https://github.com/pufereq/template-repo/commit/68f244a9e75596eb50d8e2418d4074356a1f1bf7) **rect.py**: add `PkRect` class
- [`078205e`](https://github.com/pufereq/template-repo/commit/078205e1a8671cd88fc1fff5e86ccecf25c71ced) **color.py**: add `PkColor`
- [`b2cebb9`](https://github.com/pufereq/template-repo/commit/b2cebb9e965e4e2daf516d151a5b6eae5ac44513) **object.py**: add `PkObject` class

### Miscellaneous Tasks

- [`de41155`](https://github.com/pufereq/template-repo/commit/de411556369fd5423925665c25cc896a5ac8c44e) **release.yaml**: use pyproject.toml for BUMPED_VERSION
- [`5234abe`](https://github.com/pufereq/template-repo/commit/5234abe3ba10155329eea7abd0014a761854b8b2) **release.yaml**: remove test job
- [`cbaa5c1`](https://github.com/pufereq/template-repo/commit/cbaa5c1967bfb7db48cefd4a2a4e353b61fdbc31) **release.yaml**: fix test job errors
- [`f1b2c86`](https://github.com/pufereq/template-repo/commit/f1b2c86e4ee8cee60ff2a7ae14ccde2970c4bc53) **__init__.py**: import `PkApp`
- [`c48215d`](https://github.com/pufereq/template-repo/commit/c48215d4753fb3b62c35240d818bd47224e609ae) **__init__.py**: import `PkScene`
- [`cc6a9fb`](https://github.com/pufereq/template-repo/commit/cc6a9fb2a908822eea24a40b5d5f77f7515ba4ed) **__init__.py**: import `get_texture`
- [`433cc3f`](https://github.com/pufereq/template-repo/commit/433cc3fcc5b10d925d32e020bf11768fc3286245) **__init__.py**: import `PkSubSurface`
- [`20ccfc2`](https://github.com/pufereq/template-repo/commit/20ccfc2aedd62ba4f42f0abb0e21ea03ddc25c1e) **__init__.py**: import `PkSurface`
- [`8714670`](https://github.com/pufereq/template-repo/commit/871467087b113b57852c044d7a56c6c5fef7cbd0) **__init__.py**: import `palettes`
- [`476f39e`](https://github.com/pufereq/template-repo/commit/476f39e73560dff626b933ce984f5887cec65943) **__init__.py**: import `PkRect`
- [`15fa0e2`](https://github.com/pufereq/template-repo/commit/15fa0e2157c0a53be3cffa09fba2e433f3a23521) **__init__.py**: import `PkColor` and `ColorValue` type
- [`90be9e9`](https://github.com/pufereq/template-repo/commit/90be9e936d3f6281894d799833156d3dc1fa4c74) **__init__.py**: import `PkObject`
- [`1b8f292`](https://github.com/pufereq/template-repo/commit/1b8f292976a20f286185114bed570e87cc9162ca) **test.yaml**: add coverage check
- [`6638c94`](https://github.com/pufereq/template-repo/commit/6638c9487a090f52bf82bbaddb51b8e9dcdf9fb1) **test.yaml**: change name to be more concise
- [`e473dde`](https://github.com/pufereq/template-repo/commit/e473dde0cc1a64940ddc4bfea0b3a8cca97a0ac1) **coverage.yaml**: add `name` to `comment_coverage` job

### Testing

- [`5de79c9`](https://github.com/pufereq/template-repo/commit/5de79c951dd57c73fdc9c6f316c094e470d60ed0) **test_app.py**: add tests for `app.py`
- [`7998d56`](https://github.com/pufereq/template-repo/commit/7998d56030593cbf9276d9c5db30039681388427) **test_scene.py**: add tests for `scene.py`
- [`73d76e3`](https://github.com/pufereq/template-repo/commit/73d76e3d36d6e937f85027b15aa46c06d6918e63) **test_textures.py**: add tests for `textures.py`
- [`9f3cc02`](https://github.com/pufereq/template-repo/commit/9f3cc02b32caa8c4490c6b99d111498701bba094) **test_subsurface.py**: add tests for `subsurface.py`
- [`886d579`](https://github.com/pufereq/template-repo/commit/886d57975d6c25880c7ee876da2bc70232a63761) **test_surface.py**: add tests for `surface.py`
- [`6e3df24`](https://github.com/pufereq/template-repo/commit/6e3df24de664f7a1c4af24011e3ac98367c5a49b) **test_sysfont.py**: add tests for `sysfont.py`
- [`1d425f6`](https://github.com/pufereq/template-repo/commit/1d425f69469da31177fe7d427a5cbd13d408a852) **test_font.py**: add tests for `font.py`
- [`5c04110`](https://github.com/pufereq/template-repo/commit/5c04110daf4025ba8eddd57a8b4a4769c3811a7d) **test_rect.py**: add tests for `rect.py`
- [`de54929`](https://github.com/pufereq/template-repo/commit/de54929ffe9801a2d43fe057f505a1bad04b0994) **test_color.py**: add tests for `color.py`
- [`aa455ec`](https://github.com/pufereq/template-repo/commit/aa455eceae089c4d11345f9d4227b3aca1d7b668) **test_object.py**: add tests for `object.py`

### Build

- [`17d1f1d`](https://github.com/pufereq/template-repo/commit/17d1f1d5a8505e562627133641dc44fe5f87efd6) **__init__.py**: add `puffkit/__init__.py`
- [`f46171d`](https://github.com/pufereq/template-repo/commit/f46171da1f701feb4bc4ea8e15383357e30d65ee) **.vscode/settings.json**: add testing options
- [`29485d4`](https://github.com/pufereq/template-repo/commit/29485d4d599d6ab8b612f6a8b80b3c5bb13b2131) **pyproject.toml**: set pytest to fail if coverage < 100%
- [`5468b57`](https://github.com/pufereq/template-repo/commit/5468b57f1ae53323b668574adb371075bb3c4503) **.gitignore**: add coverage information to gitignore

<!-- generated by git-cliff -->

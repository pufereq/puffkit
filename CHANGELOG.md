# Changelog

All notable changes to this project will be documented in this file.

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
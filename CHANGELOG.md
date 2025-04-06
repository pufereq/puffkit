# Changelog

All notable changes to this project will be documented in this file.

## [0.9.0] - 2025-04-06

### Bug Fixes

- [`fc61c08`](https://github.com/pufereq/template-repo/commit/fc61c08841afd91dc4b587af9839edca7e9c7077) **button_widget.py**: reorder arguments to `__init__` for consistency

### Features

- [`bc7392d`](https://github.com/pufereq/template-repo/commit/bc7392d3f96c55e566ae585b7d34cdee3151ef7b) **button_widget.py**: add `PkButtonWidget.id` attribute and `id_` argument
- [`602f3f8`](https://github.com/pufereq/template-repo/commit/602f3f8b3160800e9da03dc1e02fb16e46407a4e) **label_widget.py**: add `PkLabelWidget.id` attribute and `id_` argument
- [`a4cc51a`](https://github.com/pufereq/template-repo/commit/a4cc51a7a5e411eb50a875d85591f2ed3b9db470) **widget.py**: add `PkWidget.id` attribute
- [`6dc024d`](https://github.com/pufereq/template-repo/commit/6dc024d8246b3d312a66a80b613d83f9a11d1b2c) **container.py**: add IDs to widgets and make `PkContainer.widgets` a dict
- [`ef0d05c`](https://github.com/pufereq/template-repo/commit/ef0d05cafa359fefe66ed6924a31d36400fef2c4) **color.py**: ensure values in `PkColor`'s constructor are correct RGBA values
- [`749da55`](https://github.com/pufereq/template-repo/commit/749da559e6b71f26747a565c11b982bec86ca493) **label_widget.py**: remove `background_surface` and fill the main surface instead

### Miscellaneous Tasks

- [`3fb90a5`](https://github.com/pufereq/template-repo/commit/3fb90a589cc8798c8621ac4b02de96409240236d) **button_widget.py**: add `__str__()` `__repr__()` methods

### Refactor

- [`aa1deca`](https://github.com/pufereq/template-repo/commit/aa1deca554bf795e708baadefd4b86da7d3bfd32) **container.py**: remove `_id` argument and use `widget.id` in `PkContainer.add_widget`
- [`fbd891c`](https://github.com/pufereq/template-repo/commit/fbd891c422d23f227f2407c5329a958e7dff1af0) **container.py**: rename `_id` argument to `id_` to adhere with PEP8
- [`294dc5f`](https://github.com/pufereq/template-repo/commit/294dc5f95a12487da3a1845f254baa1488b23006) **button_widget.py**: add `id` argument to inner container's label widget
- [`7542b9c`](https://github.com/pufereq/template-repo/commit/7542b9c668239438f35d19c80779fbb04fb192cb) **container.py**: rename `children` and `child` to `widget` for clarity
- [`41fc2b4`](https://github.com/pufereq/template-repo/commit/41fc2b4c60956b47a9394c04f77de9587e39a066) **color.py**: remove redundant exception in `PkColor.from_value()`

### Testing

- [`e26c16a`](https://github.com/pufereq/template-repo/commit/e26c16a69f7a18fd00d0fe2c64f46d366773d1d5) **test_button_widget.py**: supply `PkButtonWidget.__init__()` with `id_`
- [`8bcdd92`](https://github.com/pufereq/template-repo/commit/8bcdd92fbc23153830466829bea4e60c4def6984) **test_label_widget.py**: supply `PkLabelWidget.__init__()` with `id_`
- [`9839808`](https://github.com/pufereq/template-repo/commit/9839808808514078188e8baadfaf0a7ba86a0148) **test_widget.py**: supply `PkWidget.__init__()` with `id_`
- [`b68172e`](https://github.com/pufereq/template-repo/commit/b68172ef50948f57fbc6297fa155415b8dbd6675) **test_container.py**: refactor tests to call `add_widget` with only PkWidget
- [`dcc7127`](https://github.com/pufereq/template-repo/commit/dcc7127add613c9af59d1cf4f7d16e8d138746ca) **test_container.py**: refactor tests to supply `add_widget` with ID
- [`fb59176`](https://github.com/pufereq/template-repo/commit/fb59176173c8aebec46ed5a5b5507ef2da3cb3c2) **test_container.py**: remove unused import
- [`9d25c57`](https://github.com/pufereq/template-repo/commit/9d25c57a530f27d2837e621e034bda91cdca7f85) **container.py**: adjust `PkContainer.children` to `widgets`
- [`46188e3`](https://github.com/pufereq/template-repo/commit/46188e3a25013dfe7220c651f76af580244ec678) **test_label_widget.py**: if background color is none, compare with transparent in `PkColor.from_value()` test
- [`79abd3d`](https://github.com/pufereq/template-repo/commit/79abd3d9abe5f617a431280655fa90847a4904b9) **test_color.py**: add more invalid values to test in `PkColor.from_value()`
- [`b3e8549`](https://github.com/pufereq/template-repo/commit/b3e85498550133f461b2eacdcb2fb362939b07bc) **test_color.py**: add test for invalid values in `PkColor.from_value()`

## [0.8.0] - 2025-04-06

### Bug Fixes

- [`34aea56`](https://github.com/pufereq/template-repo/commit/34aea56f37830988e4f0cdb8c30ae39f8ebe2373) **widget.py**: update `_pressed` state after calling hooks
- [`6ed64d6`](https://github.com/pufereq/template-repo/commit/6ed64d6b825b2259298724237a8c6d5f0adc70d7) **app.py**: call `scene_manager.input()` to provide events

### Features

- [`5b746b5`](https://github.com/pufereq/template-repo/commit/5b746b595b83277d2f1993296442e739f75081e6) **button_widget.py**: add the `PkButtonWidget` widget
- [`d94ea7f`](https://github.com/pufereq/template-repo/commit/d94ea7f89e038431bc84d9f52d912be0c772b931) **label_widget.py**: add `vertical_align` attribute to `PkLabelWidget`
- [`98017fb`](https://github.com/pufereq/template-repo/commit/98017fb8f7991cec2e11cb284bbc03c0f43c1a56) **widget.py**: add state attributes `_hovered`, `_pressed` and `disabled` to `PkWidget`
- [`bff18b2`](https://github.com/pufereq/template-repo/commit/bff18b253afee32ec97562d44be74a857ad52abe) **container.py**: make `PkContainer` surface-based
- [`d0774d9`](https://github.com/pufereq/template-repo/commit/d0774d9de1ebc8674cdffd6c742e517e506976bc) **widget.py**: add event handling methods
- [`23ad287`](https://github.com/pufereq/template-repo/commit/23ad287452dcad9e5b51d214512ae597af63c5f3) **event_manager.py**: add mouse position scaling to `internal_screen_size`
- [`0fc6e34`](https://github.com/pufereq/template-repo/commit/0fc6e349570685f043096ee63757ea60a4757c55) **object.py**: add `suppress_init_log` argument to PkObject's constructor

### Miscellaneous Tasks

- [`0805d4b`](https://github.com/pufereq/template-repo/commit/0805d4b693bfee461f9d25e56e3980a019061276) **widget/__init__.py**: add `PkButtonWidget` to `__init__.py`
- [`b9d6ad6`](https://github.com/pufereq/template-repo/commit/b9d6ad6d3e837bddab47ccee00c7f3d74aa7675a) **surface.py**: suppress init message for PkSurface

### Refactor

- [`57cab93`](https://github.com/pufereq/template-repo/commit/57cab933bb1e7e9398cf34bcbd4810c3a376c2dc) **widget.py**: blit the widget to container's surface
- [`df03b4f`](https://github.com/pufereq/template-repo/commit/df03b4fa109854292f60ff7e8576e23b145c3edf) **event.py**: convert event name to uppercase for compatibility

### Testing

- [`296d16d`](https://github.com/pufereq/template-repo/commit/296d16d178568349e3d96e1d5ca3d8cd32f3c235) **test_button_widget.py**: add tests for `PkButtonWidget` class
- [`aea40f3`](https://github.com/pufereq/template-repo/commit/aea40f39958851e6d18b89d98938684f19d87e47) **event_manager.py**: exclude mouse pos scaling from coverae
- [`3f53bdc`](https://github.com/pufereq/template-repo/commit/3f53bdc2e31b4e015227c8911976e42e2670f3e1) **test_event_manager.py**: modify test for `PkEventManager.update()` to test mouse pos scaling
- [`47a8ae6`](https://github.com/pufereq/template-repo/commit/47a8ae668512c014825a572f6b6382c202b64ad6) **test_widget.py**: adjust tests after refactors
- [`5078e81`](https://github.com/pufereq/template-repo/commit/5078e81338b9507329173c1e8c339715697c31a4) **test_widget.py**: add test for event handling methods
- [`db47b5d`](https://github.com/pufereq/template-repo/commit/db47b5d71182a571ac95ee0b630fe4d524b67258) **test_event.py**: correct event name to uppercase in `test_pk_event_from_pygame`

## [0.7.0] - 2025-02-23

### Bug Fixes

- [`088fa82`](https://github.com/pufereq/template-repo/commit/088fa82db11590579eb3409686937a5a5290473e) **fallback_scene.py**: correct rect supplied to `surface.blit_text()`
- [`21f7442`](https://github.com/pufereq/template-repo/commit/21f744236bb02474f58e68da99050192d6a2dfc0) **surface.py**: fix masks messing with transparency

### Documentation

- [`38c524c`](https://github.com/pufereq/template-repo/commit/38c524c43008fe57a942215920f6908ca2cf0ffd) **font.py**: update `PkFont.render()`'s docstring to include `max_width`

### Features

- [`a24659b`](https://github.com/pufereq/template-repo/commit/a24659b03a6f9a25f4187a8ffd2665b9958099fc) **font.py**: add `label` property
- [`c6f608a`](https://github.com/pufereq/template-repo/commit/c6f608a96f93d559eea5f9dd8375d185e3133a73) **surface.py**: add string and repr representations of `PkSurface`
- [`b90a2ba`](https://github.com/pufereq/template-repo/commit/b90a2ba8b18f10d4f24a32466bca7247c60cf9a8) **surface.py**: add `PkSurface.transparent` attribute
- [`41cfe02`](https://github.com/pufereq/template-repo/commit/41cfe02d883440d61a81b6d1d15dbebcb999eab2) **label_widget.py**: add `PkLabelWidget` class
- [`43cc35b`](https://github.com/pufereq/template-repo/commit/43cc35b6c7c575386a9c0ac3b2cb934430a7f38f) **surface.py**: replace `max_width` argument to `PkSurface.blit_text()` with `wrap` (bool) as max width is specified by `rect`
- [`59378d1`](https://github.com/pufereq/template-repo/commit/59378d14ab69bbb5996b877b5bc547130dac5193) **surface.py**: add `rect` argument instead of `pos`
- [`85b12c4`](https://github.com/pufereq/template-repo/commit/85b12c4bdd4d84ab851a07308ce5330ea6e252ab) **font.py**: add `align` argument to `PkFont.render()` method
- [`84e7fbd`](https://github.com/pufereq/template-repo/commit/84e7fbdaa7de217cb5cee8deadc608a1ecfbc016) **font.py**: add `PkFont.align` property
- [`1965716`](https://github.com/pufereq/template-repo/commit/196571627d9cb7be64a13369691d6629ba4cb790) **widget.py**: add the `PkWidget ` class
- [`f70b1a5`](https://github.com/pufereq/template-repo/commit/f70b1a5f6272ecb9c55bc4b2e9996f65d00d48cd) **container.py**: add `PkContainer` class
- [`44a4690`](https://github.com/pufereq/template-repo/commit/44a469035dc240004cac64215111f1bc78fe9e29) **scene.py**: fill the scene with a checkerboard on `render()` to ensure proper rendering
- [`eecd8cc`](https://github.com/pufereq/template-repo/commit/eecd8ccb165f8c6f0d5ba06e6373137d30229c7e) **surface.py**: add `PkSurface.draw_rect()` method
- [`7aa5555`](https://github.com/pufereq/template-repo/commit/7aa5555c76c6e9bb423e4c9f496308ed7c01cc38) **surface.py**: add transparency support in `PkSurface`
- [`e130d22`](https://github.com/pufereq/template-repo/commit/e130d22bae06b77692714853e9d401fb63b50c73) **app.py**: add `PkApp.get_instance()` class method to get the PkApp instance
- [`5ef90ba`](https://github.com/pufereq/template-repo/commit/5ef90baaabf1685bd1aac0851f3e75e6213a06e6) **app.py**: make PkApp a singleton (only one instance)
- [`ee5134c`](https://github.com/pufereq/template-repo/commit/ee5134cd51b98b0a8bab91075b288610ee632076) **palletes.py**: add `TRANSPARENT` color
- [`96fad1b`](https://github.com/pufereq/template-repo/commit/96fad1b171578e2a7a78543f960b0d527ed6d63b) **size.py**: add from_tuple method

### Miscellaneous Tasks

- [`67e3e60`](https://github.com/pufereq/template-repo/commit/67e3e603ff0815958029ce5a9534233bfcef8a53) **label_widget.py**: remove try/except clause in `PkLabelWidget._find_font()` as `PkSysFont` already defaults to fallback font
- [`33986f3`](https://github.com/pufereq/template-repo/commit/33986f344de2cee167c18f615f8481ef366e0200) **label_widget.py**: exclude `__str__` and `__repr__` from coverage
- [`bb36dce`](https://github.com/pufereq/template-repo/commit/bb36dce9dcc943ad9b84d5ecfee4ae185bd17513) **container.py**: exclude `__str__` and `__repr__` from coverage
- [`598cccd`](https://github.com/pufereq/template-repo/commit/598cccdbdbfd52d0b66d24bb37ef9a6318e209ad) **app.py**: remove unused `PkApp.get_instance()` method
- [`1f74f0a`](https://github.com/pufereq/template-repo/commit/1f74f0a074cafe28f8dcbab9935cf35fc272e8f1) **surface.py**: exclude `__str__` and `__repr__` from coverage
- [`32b4859`](https://github.com/pufereq/template-repo/commit/32b4859a3a66eb9c05d96d50c8a63c0272a9c31d) **fallback_scene.py**: show message every `on_render()` call
- [`bd505eb`](https://github.com/pufereq/template-repo/commit/bd505ebc48fc97eca5a709e4a6f84381fb69a3f6) **widget/__init__.py**: import `PkLabelWidget`
- [`6af5451`](https://github.com/pufereq/template-repo/commit/6af545153c69dc98757a34c84967bf9cb7188d43) **font.py**: remove PkFont's `render()` log as it will spam the logs if text is updated quickly
- [`c973afa`](https://github.com/pufereq/template-repo/commit/c973afa9ca3a59785205e631c3dbf401bbfad58d) **surface.py**: enable antialiashing by default in `PkSurface.blit_text()`
- [`72c6f27`](https://github.com/pufereq/template-repo/commit/72c6f279e95e28636d78c76447658a9972892d98) **color/__init__.py**: import `ColorValue`
- [`4cd941e`](https://github.com/pufereq/template-repo/commit/4cd941eba90342962caedc70b16127bef5faced5) **puffkit/__init__.py**: add `PkContainer` import
- [`aebbd48`](https://github.com/pufereq/template-repo/commit/aebbd4892b40f7eb6e79b11f9526835b827de703) **widget/__init__.py**: add PkWidget import
- [`ff0cfa8`](https://github.com/pufereq/template-repo/commit/ff0cfa8adfb86c8d2b3c614ea432035008fe9f47) **color/__init__.py**: add `PkColor` and `PkBasicPalette` imports
- [`637f738`](https://github.com/pufereq/template-repo/commit/637f738823c2b3c509b7120f156a7241e4f00e7c) **font/__init__.py**: add `PkFont` and `PkSysFont` imports
- [`a6c37ad`](https://github.com/pufereq/template-repo/commit/a6c37addc6dca87e4611062846ec2423ef07d5ea) **geometry/__init__.py**: import PkSize, PkRect, PkCoordinate and corresponding value types
- [`1c9fdd9`](https://github.com/pufereq/template-repo/commit/1c9fdd9740ee489cab20ab9876ea758d34241c1f) **rect.py**: make `RectValue` also accept ints

### Refactor

- [`c2d52ad`](https://github.com/pufereq/template-repo/commit/c2d52ad68441eb43c839420d8c87aac178ee6fd7) **label_widget.py**: rename `font_name` -> `font_id` for clarity
- [`c5e602e`](https://github.com/pufereq/template-repo/commit/c5e602e035d0fab1bb82f951ec190bd50ba715f9) **widget.py**: correct all `PkRect` constructor calls after refactor
- [`4cbdde5`](https://github.com/pufereq/template-repo/commit/4cbdde56738163d545e8097a2f26a9b0c0662fb2) **surface.py**: correct all `PkRect` constructor calls after refactor
- [`2169f54`](https://github.com/pufereq/template-repo/commit/2169f54501d813b458efdb7a0c62805ccdc6c8f7) **container.py**: correct all `PkRect` constructor calls after refactor
- [`d28fb1d`](https://github.com/pufereq/template-repo/commit/d28fb1dbb7a631037cfa8e13d0e5286a78afa90a) **rect.py**: refactor `PkRect`'s constructor to take `x`, `y`, `w`, `h` as arguments
- [`9a7af3b`](https://github.com/pufereq/template-repo/commit/9a7af3b3f6790fd606995aed206b321d65f926bd) **rect.py**: rename `PkRect.from_rectvalue()` to `from_tuple()` for consistency with PkSize and PkCoordinate

### Revert

- [`ea07dd7`](https://github.com/pufereq/template-repo/commit/ea07dd7672a53f03929953d761d7ea989d53791c) **app.py**: "feat(app.py): make PkApp a singleton (only one instance)"

### Styling

- [`690d045`](https://github.com/pufereq/template-repo/commit/690d0455aac56a8584487d00c73cd25eb06de2a3) **font.py**: add `PkSurface` import as TYPE_CHECKING to fix hinting
- [`fe948a7`](https://github.com/pufereq/template-repo/commit/fe948a751a1ab0df9879c0916eca0c91cc386abc) **coordinate.py**: replace `tuple[int, int]` types with  `CoordinateValue`

### Testing

- [`ea99ff5`](https://github.com/pufereq/template-repo/commit/ea99ff5f428de843e095353579bf3c5b3f1531ae) **test_label_widget.py**: add tests for `PkLabelWidget` class
- [`000f9e3`](https://github.com/pufereq/template-repo/commit/000f9e34600cc9f216d5bb4c29bbc3860a8cfe8c) **test_widget.py**: add tests for `PkWidget` class
- [`bae0d05`](https://github.com/pufereq/template-repo/commit/bae0d05db391c6b64838b6036b87399cd131f6e9) **test_container.py**: modify tests to call PkRect with `x, y, w, h` instead of `pos, size`
- [`b929870`](https://github.com/pufereq/template-repo/commit/b9298709e3cc90f2977875a9fa79d37262546d50) **test_surface.py**: modify tests to call PkRect with `x, y, w, h` instead of `pos, size`
- [`cfe7f5f`](https://github.com/pufereq/template-repo/commit/cfe7f5f68ddfccd29445be7c239a1881789f3d6d) **test_rect.py**: modify tests to use `x, y, w, h` instead of `pos, size`
- [`6916dc2`](https://github.com/pufereq/template-repo/commit/6916dc2bf2b8e04c5a974ec7730f677fa125cabf) **test_font.py**: add test for `PkFont.label` property
- [`e613d3c`](https://github.com/pufereq/template-repo/commit/e613d3cc4d729283a6f7333fc0edb2b0508a9f49) **test_container.py**: add tests for `PkContainer`
- [`c7a4fa3`](https://github.com/pufereq/template-repo/commit/c7a4fa357b2fadff109329fb9049e8734c311cf2) **test_fallback_scene.py**: add tests for `PkFallbackScene`
- [`563d247`](https://github.com/pufereq/template-repo/commit/563d2473bb7c534756e239a0272e39f01f25e0b8) **test_surface.py**: add test for `PkSurface.draw_rect()` method
- [`2e06a92`](https://github.com/pufereq/template-repo/commit/2e06a92b6591cb170f24b6d2732bed522f294cf2) **test_surface.py**: modify test for `PkSurface.blit_text()` after new functionality added
- [`64e1b89`](https://github.com/pufereq/template-repo/commit/64e1b899dc3e6c4cddd059ed82840b7be92b9bf0) **test_container.py**: add tests for `PkContainer.align` property
- [`d427340`](https://github.com/pufereq/template-repo/commit/d427340a3bacb5d25bf17f8006e5bcebf7b2e0c5) **test_size.py**: add test for `PkSize.from_tuple()` class method
- [`e21dbef`](https://github.com/pufereq/template-repo/commit/e21dbefad3875b52938ae6d71c7ba65bc027f516) **test_scene.py**: make `mock_app.internal_screen_size` a PkSize to reproduce PkApp's behavior correctly
- [`119689d`](https://github.com/pufereq/template-repo/commit/119689daa9ce673031417fbd30beab6faf266803) **test_surface.py**: add a test of transparency
- [`25a1ccf`](https://github.com/pufereq/template-repo/commit/25a1ccf6f677eb228a0ac7805c45ea890ad3c9f2) **test_rect.py**: alter `PkRect.from_tuple()` tests after rename

### Build

- [`bcb9107`](https://github.com/pufereq/template-repo/commit/bcb9107fbe91df1700bba408dd14697028cb87b8) **.vscode/settings.json**: change mode from 755 to 644

## [0.6.0] - 2024-12-31

### Bug Fixes

- [`1d5e311`](https://github.com/pufereq/template-repo/commit/1d5e31174803ce70caa2285d450c336099a9e5f5) **scene_manager.py**: do not supress errors on scene loading in `set_scene()`
- [`712d31b`](https://github.com/pufereq/template-repo/commit/712d31bb24b7a160f973c4230b7f92fae9178780) **event_manager.py**: fix wrong `input()` call, now points to `self.app.scene_manager.input()`
- [`bd15b2f`](https://github.com/pufereq/template-repo/commit/bd15b2f5bff1c3b7511f89918f3e4c4b6a41a340) **scene.py**: fix `loaded` being set even if loading failed

### Features

- [`47b0ed0`](https://github.com/pufereq/template-repo/commit/47b0ed0198a2b7098f579851fae10e0a8b7c2e74) **scene_manager.py**: add `PkSceneManager.load_scene()` method to avoid redundancy in scene loading
- [`4af00af`](https://github.com/pufereq/template-repo/commit/4af00af0066d7ac04e7f0a3cd6a5538286875e2d) **scene_manager.py**: implement scene load error handling in `PkSceneManager.set_scene()`
- [`37d9ea3`](https://github.com/pufereq/template-repo/commit/37d9ea3a2d83ca1b78b0da8af2c14bc5b29d6a20) **scene.py**: add `PkScene.auto_unload` attribute which will determine if the scene will be unloaded when changing the current scene
- [`5f780e7`](https://github.com/pufereq/template-repo/commit/5f780e72992319a6795e200771e89df0749fe179) **scene_manager.py**: add a timer on `PkScene.load()` and display time taken
- [`8466ae2`](https://github.com/pufereq/template-repo/commit/8466ae29bff51ea4040f9560d6ff325aac7f2624) **scene_manager.py**: handle duplicate scenes by showing the exception on fallback scene
- [`d0df5db`](https://github.com/pufereq/template-repo/commit/d0df5db470275594d5147e30a7d7e45d190b492a) **scene_manager.py**: add `PkFallbackScene` to Scene Manager
- [`04c38df`](https://github.com/pufereq/template-repo/commit/04c38dfad21b59c3a3ad908fe235f036e1da11e8) **fallback_scene.py**: add `PkFallbackScene` class
- [`34361eb`](https://github.com/pufereq/template-repo/commit/34361ebe3fc0664e9a9c1149195d2a72d524a427) **app.py**: implement `PkSceneManager` and remove scene management from `PkApp`
- [`297adb5`](https://github.com/pufereq/template-repo/commit/297adb5917181c2b338cef1fbd8e676ee5ad4bf7) **scene_manager.py**: add `PkSceneManager`

### Miscellaneous Tasks

- [`3eec703`](https://github.com/pufereq/template-repo/commit/3eec7036a5e3a08a7d34e4482172103acec3c7f6) **scene_manager.py**: log unload success in `PkSceneManager.unload_scene()`
- [`52f41eb`](https://github.com/pufereq/template-repo/commit/52f41eb9543bb1908d7cf67f2379159cd2f75c79) **pyproject.toml**: update depedencies
- [`ad8591a`](https://github.com/pufereq/template-repo/commit/ad8591a442923e74fd188a8b3bf615fbdf8c4f3f) **scene.py**: exclude type imports from coverage
- [`3fbc5a3`](https://github.com/pufereq/template-repo/commit/3fbc5a3c0e62a5d7b6d7858cdc32085aaa6ae06f) **scene_manager.py**: add auto unloading support to `PkSceneManager.set_scene()`
- [`c26c4a4`](https://github.com/pufereq/template-repo/commit/c26c4a4022e3d1c314c771bfed7496663922cfa5) **scene.py**: remove error handling from `PkScene.load()` as they will be handled in manager
- [`2227b38`](https://github.com/pufereq/template-repo/commit/2227b38f51045d61eb4d720ea3b643713a972e81) **scene.py**: remove call to `PkScene.load()` from `__init__()`
- [`d81ee47`](https://github.com/pufereq/template-repo/commit/d81ee476f0a5c6468992480f5748644daac6bc5c) **scene_manager.py**: log scene count after `add_scene()` and `remove_scene()` methods
- [`248dd45`](https://github.com/pufereq/template-repo/commit/248dd45721b4b782498c97d11494aaf7cc8a62fc) **scene/__init__.py**: add `__init__.py` to `scene` module
- [`eafc97b`](https://github.com/pufereq/template-repo/commit/eafc97be8da3408777d03223d5657d175a55525e) **scene.py**: turn on antialiasing for scene loading error text
- [`85191ac`](https://github.com/pufereq/template-repo/commit/85191acece967e30fb0013c36afe16a3c64b7d9f) **app.py**: change the `default` font size to 14px
- [`622aaae`](https://github.com/pufereq/template-repo/commit/622aaae68a0e3b0cc7a8c57bb70d7a4376ffaa2c) **scene.py**: move `scene.py` to `puffkit/scene/scene.py`
- [`4652820`](https://github.com/pufereq/template-repo/commit/46528206a80b3f284fe8010104571272efe0b8d0) **release.yaml**: recurse submodules on checkout

### Refactor

- [`46d2ce3`](https://github.com/pufereq/template-repo/commit/46d2ce36e804b4ab3f6365c1d316a26e39ec0a01) **scene_manager.py**: call `PkSceneManager.unload_scene()` instead of unloading manually in `set_scene()`
- [`aab9e65`](https://github.com/pufereq/template-repo/commit/aab9e6560230c85aaa8d4280e19289791d2a9078) **scene_manager.py**: use the `PkSceneManager.load_scene()` method in `set_scene()`
- [`dbcb13d`](https://github.com/pufereq/template-repo/commit/dbcb13dc76a8b20080cef47cb9a670ab2072395d) **scene_manager.py**: use the `PkSceneManager.load_scene()` method in `add_scene()`
- [`dc46e57`](https://github.com/pufereq/template-repo/commit/dc46e57d085bb281fd25ea57370ca3cc38c8bed0) **scene_manager.py**: remove unnecesarry if statements in input, update and render methods
- [`e6f5cca`](https://github.com/pufereq/template-repo/commit/e6f5cca3caf5cb4cb5139c3b8b109f17db42d0e6) **event_manager.py**: modify `PkEventManager.update()` method to reference scene manager

### Styling

- [`d51b12a`](https://github.com/pufereq/template-repo/commit/d51b12a486497ab926416897f10952fe027877f5) **scene.py**: remove unnecesarry imports

### Testing

- [`8e36052`](https://github.com/pufereq/template-repo/commit/8e36052947f2609b923dbf94c4abc8c2f0ce7f1a) **test_scene_manager.py**: add tests for `PkSceneManager.load_scene()` method
- [`ccf6a50`](https://github.com/pufereq/template-repo/commit/ccf6a50fd8a34740b238df4399014a4b7957e656) **test_scene_manager.py**: make mock_scene lazy
- [`201ba25`](https://github.com/pufereq/template-repo/commit/201ba25eb3338080a234ab8c8e911999765a50c7) **test_scene_manager.py**: fix badly written `test_set_scene_load_error()` test
- [`9748a34`](https://github.com/pufereq/template-repo/commit/9748a341a8f70ff179d5c6e5a16d1547c9a93585) **test_scene.py**: add test for `PkScene.draw()`
- [`a254c72`](https://github.com/pufereq/template-repo/commit/a254c72b047c564094a47df373f91c2e21859e9b) **test_scene_manager.py**: add tests for errors, lazy and auto-unload scenes
- [`503aaf0`](https://github.com/pufereq/template-repo/commit/503aaf032b8cf0c7db253323d6987cb4b4f889bd) **test_scene_manager.py**: add a `PkScene()` fixture
- [`5d8064f`](https://github.com/pufereq/template-repo/commit/5d8064f142b40fea0e8af33c665a3670cb10af87) **test_timing.py**: add tests for the `timing.py` module (`Timer` class, `measure_execution_time` decorator)
- [`fe93f6e`](https://github.com/pufereq/template-repo/commit/fe93f6e61d0f27f4dc2f88a377014d5172a691b3) **test_scene.py**: add tests for `on_load`, `on_unload`, `on_update` and `on_render` methods
- [`8e3f648`](https://github.com/pufereq/template-repo/commit/8e3f6482908141efbae654a747db64689318967a) **test_event_manager.py**: fix incorrect assert in `test_update()`
- [`764791d`](https://github.com/pufereq/template-repo/commit/764791de6814f85b94ea0d75107e5e8cecbccc2f) **test_event_manager.py**: add type hints in tests
- [`4cfa128`](https://github.com/pufereq/template-repo/commit/4cfa1283e03a43d80040dc3599c7c171ad8f7a0c) **test_event_manager.py**: replace `app` (argument)'s type to PkAppSubclass from Mock in `event_manager` fixture
- [`7a68967`](https://github.com/pufereq/template-repo/commit/7a6896711a5feb5e48b53459387855eb1a3549a7) **test_event_manager.py**: replace PkApp's mock with a real PkApp
- [`6bd72a4`](https://github.com/pufereq/template-repo/commit/6bd72a40754e58158fde3e396d18d9b307fcb9b0) **test_scene_manager.py**: check for `fallback` scene being loaded when a duplicate scene is added instead of exception
- [`4bc4cbd`](https://github.com/pufereq/template-repo/commit/4bc4cbd7d6e5f97b0398b09b9f3f462300b42b29) **test_scene_manager.py**: add `"fallback"` to loaded scenes assertion in `test_loaded_scenes()`
- [`92c39d2`](https://github.com/pufereq/template-repo/commit/92c39d2112c4b64e8af1b35409ce3d8a77c2153a) **test_scene_manager.py**: add `auto_unload` attribute to `mock_scene()`
- [`055a445`](https://github.com/pufereq/template-repo/commit/055a445da7a7b02b08b4964abf1003ebecba29cc) **test_scene_manager.py**: replace PkApp's mock with a real PkApp
- [`b2856c9`](https://github.com/pufereq/template-repo/commit/b2856c9cd502703a0cd3b7bfaa1fd0be09373c9a) **test_scene.py**: refactor tests for `PkScene` after `PkSceneManager`'s addition
- [`1bd0c16`](https://github.com/pufereq/template-repo/commit/1bd0c1600f0d5e4cdf649df4b3ebe0d8d9b8f2f6) **test_app.py**: remove non-existent methods' tests
- [`fd4aa9e`](https://github.com/pufereq/template-repo/commit/fd4aa9ebb17db55c755b2fd021fb7f5f88aa5b6d) **test_scene_manager.py**: add tests for `PkSceneManager` class
- [`77d91e6`](https://github.com/pufereq/template-repo/commit/77d91e6328380f9d6db9373bb90437f5921b33ae) **test_scene.py**: move `tests/scene.py` to `tests/scene/scene.py`

## [0.5.0] - 2024-12-11

### Bug Fixes

- [`bb8458b`](https://github.com/pufereq/template-repo/commit/bb8458b03a930d63f53609ae145c61743ca6da8d) **event_manager.py**: move `PkApp` import to `TYPE_CHECKING` to avoid circular import
- [`135faae`](https://github.com/pufereq/template-repo/commit/135faae76def96ea9601f76f281c3b206883360d) **app.py**: fix no `internal_screen` scaling being applied in `PkApp.render()`

### Documentation

- [`60f8b02`](https://github.com/pufereq/template-repo/commit/60f8b029b05eef304526deb3b9c5073f4e0817f5) **event_manager.py**: improve docstrings
- [`b56bc74`](https://github.com/pufereq/template-repo/commit/b56bc746f52f9a783d59efc090b93908dfd3c3ea) **app.py**: add missing arguments to `PkApp`'s docstring

### Features

- [`c3ac7d9`](https://github.com/pufereq/template-repo/commit/c3ac7d9a84f7f9d5fd9fcc602021cff6c4299d82) **event.py**: replace `PkEvent.type` attribute with `PkEvent.name` of type `str`
- [`d354147`](https://github.com/pufereq/template-repo/commit/d354147e2657b1a9d46d21d949383f34acf32c5d) **app.py**: implement `PkEventManager` in PkApp
- [`5de80af`](https://github.com/pufereq/template-repo/commit/5de80afd4deadfe720dc2a08fc52977beb62131d) **event_manager.py**: add the event manager `PkEventManager`
- [`c1e1740`](https://github.com/pufereq/template-repo/commit/c1e1740d27ec700e1c74a16c4acf6a5da8f7cecc) **event.py**: add `PkEvent` class
- [`4f340f8`](https://github.com/pufereq/template-repo/commit/4f340f801599656b6a890cad11e9309319a9023a) **event_constants.py**: add `PkEventConstants` class
- [`367b1bd`](https://github.com/pufereq/template-repo/commit/367b1bd42a2f980b60661f5ff662ef446d84d6b8) **scene.py**: add `on_load()`, `on_update()`, `on_render()` hooks to PkScene
- [`4cf4721`](https://github.com/pufereq/template-repo/commit/4cf4721934ee36f0c544075b262b5350028fbf72) **app.py**: set window title based on app name, version and FPS
- [`35c0a71`](https://github.com/pufereq/template-repo/commit/35c0a71e1bb0d8c979863c87c885304ca4b88ae4) **timing.py**: add timing decorators
- [`3e7f78a`](https://github.com/pufereq/template-repo/commit/3e7f78a2233e3807d41aa8368fedaaf50985b356) **coordinate.py**: add `PkCoordinate.tuple` property
- [`80021a1`](https://github.com/pufereq/template-repo/commit/80021a1e19ede1e8fdd70b4a5c963db574a397fa) **size.py**: add `PkSize.tuple` property

### Miscellaneous Tasks

- [`4a0965b`](https://github.com/pufereq/template-repo/commit/4a0965b7e59c7f9ded8c9a8bd70aeb94fad3bef8) **event/__init__.py**: remove `PkEventConstants` import
- [`320d37c`](https://github.com/pufereq/template-repo/commit/320d37cbb86901c565b358188a6858674da0f326) **event_constants.py**: remove unused `event_constants` module
- [`020a20d`](https://github.com/pufereq/template-repo/commit/020a20db87065a7eb3ace68320d3aca2bb0e6201) **event_manager.py**: input received events to the active scene
- [`0c9bd1c`](https://github.com/pufereq/template-repo/commit/0c9bd1ca51c543518b3a56fca2542c91619121dc) **app.py**: remove obsolete `PkApp.handle_events()` method
- [`9d006de`](https://github.com/pufereq/template-repo/commit/9d006dec77c5ba767bce29f9cf8554e7b657f093) **event/__init__.py**: add __init__.py to event module
- [`49597bb`](https://github.com/pufereq/template-repo/commit/49597bbad50ee793b2c120ba884f81905be2cf04) **scene.py**: exclude `__str__` and `__repr__` from coverage
- [`6b34b83`](https://github.com/pufereq/template-repo/commit/6b34b83d309d92a32e70481b221c25edf7dd205f) **scene.py**: add str and repr method
- [`bf4b92c`](https://github.com/pufereq/template-repo/commit/bf4b92c1149143fcfc3f9f575e3688d9258accc2) **app.py**: make `PkApp.scenes` a final (const)
- [`6ead962`](https://github.com/pufereq/template-repo/commit/6ead9623a18d05dab2c36fbabdbf4b6fe39886db) **app.py**: use the `display_size.tuple` property instead of `tuple(display_size)`
- [`5b511a3`](https://github.com/pufereq/template-repo/commit/5b511a3d8ebb54bb3437a8fc152ffc1d8429b01b) **surface.py**: add support for `SizeValue` and `CoordinateValue` in `PkSurface`
- [`ab8806f`](https://github.com/pufereq/template-repo/commit/ab8806f0cc56297acef05201c71e2ab03ec18906) **coordinate.py**: add `CoordinateValue` type
- [`96862fe`](https://github.com/pufereq/template-repo/commit/96862fe2f1db1c0f50e94461c02f9636d085d84d) **size.py**: add `SizeValue` type

### Refactor

- [`9e09884`](https://github.com/pufereq/template-repo/commit/9e098842fd1779bf1b9e3ad20debf5d20f875456) **event.py**: rename references to `PkEvent.type` to `PkEvent.name`
- [`87960ba`](https://github.com/pufereq/template-repo/commit/87960bad097dd81f641ef57bc7a7ed58b36c5e12) **puffkit/__init__.py**: move imports to the top of the module
- [`6b83da9`](https://github.com/pufereq/template-repo/commit/6b83da98ffae3214386ddde14e18b31df7dbe994) **app.py**: modify references to `PkScene.init()` and `PkScene.initialized` after rename
- [`3fb8f91`](https://github.com/pufereq/template-repo/commit/3fb8f911dd632e1c66e1abb921f56098e33a1029) **scene.py**: rename `PkScene.init()` to `load()` as it shows the purpose better
- [`8091071`](https://github.com/pufereq/template-repo/commit/8091071089f888f77766bf2a141b50becfa23e0f) **scene.py**: rename `PkScene.initialized` to `loaded`
- [`aca19fe`](https://github.com/pufereq/template-repo/commit/aca19feeab5e429dff2bb2e5189cc1a77919f912) **app.py**: rename `PkApp.fps` to `fps_limit` for clarity

### Testing

- [`ebe6d3c`](https://github.com/pufereq/template-repo/commit/ebe6d3c853d6cb2844dcdbc22e08d552ecf01d55) **test_event_manager.py**: adapt tests to changes in `PkEventManager`
- [`dd62d7b`](https://github.com/pufereq/template-repo/commit/dd62d7bbf44ce5efe07b54db6df90bd0bcd10a37) **test_event.py**: adapt tests to changes in `PkEvent`
- [`aa604e8`](https://github.com/pufereq/template-repo/commit/aa604e8cb86b335d8ce65f22505350a6787856bb) **event.py**: exclude `__str__` and `__repr__` from coverage
- [`26af623`](https://github.com/pufereq/template-repo/commit/26af623844094fa6c930adc33f2a0790b9084ea9) **test_app.py**: remove `PkApp.handle_events()`-specific tests as it is removed
- [`61e234a`](https://github.com/pufereq/template-repo/commit/61e234a6ac38c37b70c12d975d7847c53e4bdd46) **test_event_manager.py**: initialize pygame before creating a event manager instance
- [`d70837c`](https://github.com/pufereq/template-repo/commit/d70837cd095d2bd9e4390314f075e890f234a4ca) **test_event_manager.py**: add tests for the `PkEventManager` class
- [`d3b6371`](https://github.com/pufereq/template-repo/commit/d3b6371c536413dfa95a9967cf57d93e6be5c79b) **test_event.py**: add tests for the `PkEvent` class
- [`eac8cf2`](https://github.com/pufereq/template-repo/commit/eac8cf26ab6f293a0bf16b8339c8c96110f82e62) **test_app.py**: rename references to `PkScene.loaded` after rename
- [`ed37bc6`](https://github.com/pufereq/template-repo/commit/ed37bc666d4577796305249baef8471655b140d8) **test_app.py**: refactor tests to reflect on `PkApp.fps_limit` rename

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

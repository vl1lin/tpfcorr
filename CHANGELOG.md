# Changelog

Формат — [Keep a Changelog](https://keepachangelog.com/ru/1.1.0/), версии — [SemVer](https://semver.org/lang/ru/).
До `1.0.0` минорные версии могут ломать API.

## [0.1.0a1] — 2026-11-12

Первый предрелиз.

### Добавлено
- Корреляции: `beggs_brill`, `mukherjee_brill`, `hasan_kabir`, `ansari`.
- Модели режима течения: `beggs_brill_map`, `mukherjee_brill_fp`, `taitel_dukler`, `barnea`,
  `hasan_kabir_fp`, `ansari_fp`.
- Реестр (`get_correlation`, `get_flow_model`, `list_*`, `describe_*`), `FlowState`, `FlowPattern`,
  опции моделей (pydantic), ошибки и предупреждения.
- `tpfcorr.__version__`.
- Лицензия MIT.

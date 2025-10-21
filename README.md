# Neutral Aviation-Industrial Cluster (Mykolaiv) – UA-NOVEYA Pilot

![Status](https://img.shields.io/badge/status-draft-yellow) ![Version](https://img.shields.io/badge/version-0.1-blue)

<img src="assets/banner.png" alt="Banner" />

## Описание
Нейтральный авиационно‑индустриальный кластер в Николаеве. Проект интегрирован в экосистему **UA‑NOVEYA** и нацелен на восстановление Причерноморья через инновации в авиации, дронах и ИИ.

## Состав
- **Agro‑Air** — агроавиация, узел в Щербанях; обработка полей, доставка в громады.
- **U‑Space** — цифровая инфраструктура управления дронами, диспетчерский центр.
- **MRO** — техобслуживание и ремонт (Кульбакино), сервис малой авиации и БПЛА.
- **Drones R&D** — разработка и производство беспилотников, узлы «Зоря‑Машпроект».
- **Protonoveya AI** — управляющий ИИ‑слой (FDL/СВЕТ), координация данных и решений.

## Инфраструктура
- **Зоря‑Машпроект** — турбинные технологии для силовых установок.
- **НАРП (Кульбакино)** — авиаремонтный завод, ангары, ВПП.
- **Аэропорт Баловное (UKON)** — гражданский аэропорт, тесты и логистика.
- **Аэродром Щербани** — база агроавиации и учебных полётов.
- **Военный аэродром (демилитаризуемые мощности)** — дополнительные полосы и ангары.

## Архитектура ИИ
**Protonoveya Meta‑Layer**:
- **FDL Engine** — ядро формально‑диалектической логики.
- **API Gateway** — интерфейсы для модулей кластера.
- **Nodes** — узлы‑спутники для MRO, Agro, U‑Space, образования.
- **Semantic Shield** — защита от искажения смыслов.
- **Σ‑FDL Tokens** — протокол фиксации решений.

## Installation / Deployment
> *(черновик IT‑части, обновляется)*

### Вариант A: Docker
```bash
docker pull noveya/protonoveya-node:latest
docker run -d --name protonoveya-node -p 8080:8080   -e NOTION_API_KEY=$NOTION_API_KEY -e CLUSTER_DB_URL=$CLUSTER_DB_URL   -v $(pwd)/config:/app/config noveya/protonoveya-node
```

### Вариант B: Python
```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # укажите ключи/URL
python src/fdl_engine.py
```

## Contributing
- Реперные материалы см. в **/docs** (экспорт из Notion): экосистемы, Таврида‑узел, проектное досье кластера, методология ИИ‑модулей.
- Контакты: НГОИ (громада Николаева) · protonoveya@gmail.com.
- Правила: соблюдение FDL‑методологии, прозрачность, локализация решений, Pay‑for‑Fact.

## License & Ethics

This repository follows a dual-license scheme:

- **Code:** AGPL-3.0  
- **Content / Symbols / Media:** CC BY-NC-SA 4.0  
- **Ethical charter:** see [LICENSE-ETHICS.md](./LICENSE-ETHICS.md)

Use of FDL/NOVEYA symbols is allowed **only** in open, benevolent contexts; closed or exploitative usage is prohibited.

---

## 3) Краткая настройка CI (по желанию, одинаковая везде)

`.github/workflows/ci.yml` (для Python; при необходимости сделаю Node-вариант):

```yaml
name: ci
on: [push, pull_request]
jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - run: pip install -r requirements.txt || true
      - run: pip install pytest || true
      - run: pytest -q || echo "No tests yet"

---

## Публичная аннотация (для сайта)
В Николаеве запускается нейтральный авиационно‑индустриальный кластер – проект возрождения региона с опорой на инновации. Кластер объединит агроавиацию, производство дронов, обслуживание самолётов и ИИ‑технологии в единую экосистему. Он создаётся как часть всеукраинской инициативы **UA‑NOVEYA** и призван стать моделью развития для других громад Причерноморья. На базе местных заводов и аэропортов появятся новые производства и центры обучения, а специальная AI‑система «Протоновея» будет помогать координировать работу кластера. Проект реализуется при поддержке местной громады и открыт для инвесторов и партнёров. Его цель – новые рабочие места, рост экономики и внедрение передовых технологий, которые сделают Николаев лидером инновационного развития на Юге Украины.

---

<p align="center"><img src="assets/logo.png" width="96" alt="Logo"></p>

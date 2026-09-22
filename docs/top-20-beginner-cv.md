# Top 20: beginner ∩ CV fit (yüksek güven, az kişi)

Kaynak sınıflandırma: `data/oh-my-pi-issue-classifications.json`.
Tam katalog: [`issues.md`](issues.md).

CV referansı: adayın TypeScript + Python + Rust, LangGraph/RAG ajanları,
CLI/TUI (Apex/Textual), FastAPI/React ve GitHub Actions deneyimi. oh-my-pi
tarafında bu, **prompt/tool/CLI/TUI/agent** işlerine denk geliyor; saf macOS
native veya derin protocol RFC’leri değil.

## Seçim kuralı

Bu liste **gözlenen aktiviteye** dayanır; assignee yokluğu veya mention’sız bir dal “iş yapılmıyor” demek değildir.

1. Jev **beginner-friendly = evet** ve **CV fit = evet** (eşik 0.5).
2. `wontfix` / `duplicate` yok.
3. **Gözlenen açık PR yok** — 1769 issue timeline (`CrossReferencedEvent` / `CONNECTED_EVENT`: open/merged/closed) **artı** 1092 açık PR’de `closingIssuesReferences` ve başlıktaki `#N`.
4. **Gözlenen aktif katkıcı = 0**: botlar hariç insan yorumcu + *açık* PR yazarı. Issue yazarı bu sayıya **yalnız** ilerleme beyanı varsa girer (“working implementation”, “tests ready”, “PR incoming”, “I’m working on this”). Yalnız issue açmak sayılmaz. Assignee 1769/1769 boş; “kimse üstlenmedi” denmez.
5. Sıra: `0.55 × √(beginner_noul × cv_noul) + 0.45 × difficulty_confidence`; gözlenen açık PR, kalabalık ve yazar-ilerleme beyanı düşürür.

187 kullanılabilir kesişimden 46’sında *gözlenen* açık PR vardı; onlar elendi. [#4993](https://github.com/can1357/oh-my-pi/issues/4993) yazarın “implementation + tests ready” beyanı yüzünden (gözlenen katkıcı = 1, hazır implementasyon iddiası) listeden çıktı. Kalanlarda confidence yüksek ve bu sinyallerde rakip görünmeyen işler öne çıktı.

**Aktivite (2026-09-19):** Tüm 1769 issue timeline (hiçbiri `hasNextPage`); açık PR = 1092; assignee = 0/1769. Katalog özeti: bağlı PR (herhangi durumda) 564 · açık 389 · merged 121 · closed-unmerged 200.

## Tablo

| # | Issue | Zorluk | Beg noul | CV noul | Diff conf | Gözlenen açık PR | Gözlenen katkıcı | Neden kısa |
|---|---|---|---:|---:|---:|---|---:|---|
| 1 | [#8801](https://github.com/can1357/oh-my-pi/issues/8801) | easy | 0.83 | 0.57 | 1.00 | yok | 0 | Tek markdown: `AGENTS.md` |
| 2 | [#5951](https://github.com/can1357/oh-my-pi/issues/5951) | easy | 0.82 | 0.56 | 0.99 | yok | 0 | Status line: `auto → high` |
| 3 | [#7225](https://github.com/can1357/oh-my-pi/issues/7225) | easy | 0.84 | 0.53 | 1.00 | yok | 0 | Fazladan `Buffer.from` kopyası |
| 4 | [#10960](https://github.com/can1357/oh-my-pi/issues/10960) | easy | 0.81 | 0.59 | 0.97 | yok | 0 | Recall success debug log |
| 5 | [#7891](https://github.com/can1357/oh-my-pi/issues/7891) | easy | 0.78 | 0.61 | 0.96 | yok | 0 | Docs + küçük UX, session hygiene |
| 6 | [#11319](https://github.com/can1357/oh-my-pi/issues/11319) | easy | 0.81 | 0.51 | 1.00 | yok* | 0 | `bash.md` sqlite3 yasağı |
| 7 | [#7204](https://github.com/can1357/oh-my-pi/issues/7204) | easy | 0.68 | 0.58 | 0.96 | yok | 0 | Shake min token eşiği |
| 8 | [#12255](https://github.com/can1357/oh-my-pi/issues/12255) | easy | 0.68 | 0.60 | 0.94 | yok | 0 | Architect JSON fence regex |
| 9 | [#11605](https://github.com/can1357/oh-my-pi/issues/11605) | mid | 0.55 | 0.62 | 0.98 | yok | 0 | Collab web dosya upload |
| 10 | [#8729](https://github.com/can1357/oh-my-pi/issues/8729) | easy | 0.68 | 0.54 | 0.95 | yok | 0 | `biome check --write` |
| 11 | [#6094](https://github.com/can1357/oh-my-pi/issues/6094) | mid | 0.57 | 0.56 | 0.97 | yok | 0 | `display.currencySymbol` |
| 12 | [#11096](https://github.com/can1357/oh-my-pi/issues/11096) | mid | 0.60 | 0.55 | 0.95 | yok | 0 | `browser-relay status` |
| 13 | [#7052](https://github.com/can1357/oh-my-pi/issues/7052) | mid | 0.61 | 0.62 | 0.87 | yok | 0 | `omp stats` CSV export |
| 14 | [#7076](https://github.com/can1357/oh-my-pi/issues/7076) | easy | 0.78 | 0.56 | 0.81 | yok | 0 | `stats --no-open` |
| 15 | [#11145](https://github.com/can1357/oh-my-pi/issues/11145) | mid | 0.62 | 0.55 | 0.89 | yok | 0 | Ask Submit tab notu |
| 16 | [#5346](https://github.com/can1357/oh-my-pi/issues/5346) | easy | 0.82 | 0.54 | 0.79 | yok | 0 | Mesaj datetime |
| 17 | [#10943](https://github.com/can1357/oh-my-pi/issues/10943) | mid | 0.63 | 0.54 | 0.89 | yok | 0 | `/review` mode notu |
| 18 | [#5674](https://github.com/can1357/oh-my-pi/issues/5674) | mid | 0.66 | 0.55 | 0.85 | yok | 0 | vibe `fast`/`good` config |
| 19 | [#10887](https://github.com/can1357/oh-my-pi/issues/10887) | easy | 0.75 | 0.54 | 0.80 | yok | 0 | Truncation notice sayaçları |
| 20 | [#4807](https://github.com/can1357/oh-my-pi/issues/4807) | mid | 0.60 | 0.55 | 0.87 | yok | 0 | `skill://` vb. URL vurgusu |

\* [#11319](https://github.com/can1357/oh-my-pi/issues/11319): açık PR yok; kapanmış merge’süz [#11591](https://github.com/can1357/oh-my-pi/pull/11591) var — iş bitmemiş.

İlk PR için pratik sıra: **8801 → 10960 → 7076 → 7225 → 5951**. Hepsi dar ve çakışmasız.

---

## 1. [#8801](https://github.com/can1357/oh-my-pi/issues/8801) — architect prompt’a `AGENTS.md`

**Skor:** beginner 0.83 · CV 0.57 · difficulty easy / conf **1.00** · gözlenen aktif katkıcı 0 · gözlenen açık PR yok.

**Neden seçildi.** `agent-creation-architect.md` içinde iki yerde yalnız `CLAUDE.md` geçiyor. Native projede talimat `.omp/AGENTS.md`. Issue tam cümle önerisi veriyor.

**Confidence neden yüksek.** Scope bir dosya, iki string. Mimari yok. Easy neredeyse kesin (conf 1.00). Beginner 0.83 “docs/prompt copy” kalıbı. CV 0.57 eşikte-üstü: ajan prompt’u, resume’daki LangGraph/agent işiyle örtüşür.

**Gözlenen ilerleme.** Timeline’da yorumcu / açık / merged / closed PR yok. Bağlantısız çalışma görünmez.

## 2. [#5951](https://github.com/can1357/oh-my-pi/issues/5951) — auto thinking hâlâ auto

**Skor:** 0.82 / 0.56 / easy 0.99 · gözlenen aktif katkıcı 0 · gözlenen açık PR yok.

**Neden.** Status line `auto` iken tur sınıflanınca yalnız `high` kalıyor; kullanıcı auto’nun kapandığını sanıyor. Öneri: `auto → high` veya `high (auto)`.

**Confidence.** TUI’de tek görüntü kuralı. Diff conf 0.99. CV, resume’daki TUI (Apex/Textual) + UX ile hizalı.

**Gözlenen ilerleme.** Yorumcu ve bağlı PR yok (gözlenen aktif katkıcı 0). Üstlenilmediği iddia edilmez.

## 3. [#7225](https://github.com/can1357/oh-my-pi/issues/7225) — `loadImageInput` Buffer kopyası

**Skor:** 0.84 / 0.53 / easy **1.00** · gözlenen aktif katkıcı 0 · gözlenen açık PR yok.

**Neden.** `fs.readFile` zaten `Buffer` döner; `Buffer.from(inputBuffer).toBase64()` gereksiz kopya. Satır ve Node dokümanı issue’da.

**Confidence.** Beginner 0.84, zorluk conf 1.00: tek fonksiyon, davranış değişmez. CV 0.53 ince (saf perf) ama TypeScript runtime resume dillerine uyuyor.

**Gözlenen ilerleme.** Yorumcu ve bağlı PR yok.

## 4. [#10960](https://github.com/can1357/oh-my-pi/issues/10960) — Hindsight recall success log

**Skor:** 0.81 / 0.59 / easy 0.97 · gözlenen aktif katkıcı 0 · gözlenen açık PR yok.

**Neden.** `hindsight.debug: true` iken retain ve recall-fail loglanıyor, başarılı recall sessiz. 378 log dosyasında 0 success satırı. İstenen: item count + duration.

**Confidence.** Mevcut debug guard’ı simetriklemek. Agent/memory hattı resume’daki RAG/LangGraph ile CV 0.59.

**Gözlenen ilerleme.** Yorumcu ve bağlı PR yok.

## 5. [#7891](https://github.com/can1357/oh-my-pi/issues/7891) — otomasyon session hygiene (docs)

**Skor:** 0.78 / 0.61 / easy 0.96 · gözlenen aktif katkıcı 0 · gözlenen açık PR yok.

**Neden.** `--no-session`, `--session-dir`, nested sidecar zaten var; eksik keşfedilebilirlik. Yazar “docs + küçük UX, storage redesign değil” diyor.

**Confidence.** Easy çünkü yeni persist modeli yok. CV 0.61 listedeki en yükseklerden: CLI ürün + ajan oturumları.

**Gözlenen ilerleme.** Yazar PR açmayacağını yazmış; timeline’da başka yorumcu/PR yok.

## 6. [#11319](https://github.com/can1357/oh-my-pi/issues/11319) — bash `<critical>` + sqlite3

**Skor:** 0.81 / 0.51 / easy **1.00** · gözlenen aktif katkıcı 0 · gözlenen açık PR yok.

**Neden.** `read` SQLite selector’ları var; `bash.md` yasağı `sqlite3` demiyor, model 15 kez shell’e kaçıyor. Önerilen Handlebars satırı issue’da.

**Confidence.** “Prompt text only; no schema or runtime change.” Easy conf 1.00. CV 0.51 zayıf-eşik; yine tool/prompt.

**Gözlenen ilerleme.** Açık PR yok. Timeline’da kapanmış merge’süz [#11591](https://github.com/can1357/oh-my-pi/pull/11591). Issue hâlâ açık; iş bitmiş sayılmaz.

## 7. [#7204](https://github.com/can1357/oh-my-pi/issues/7204) — shake tool-result min tokens

**Skor:** 0.68 / 0.58 / easy 0.96 · gözlenen aktif katkıcı 0 · gözlenen açık PR yok.

**Neden.** 5 token’lık tool result ~20 token’lık recovery pointer ile yer değiştiriyor. `toolResultMinTokens` (20–25) `ShakeConfig`’e.

**Confidence.** Tek eşik, mevcut `fenceMinTokens: 400` ile aynı fikir. Context-compaction / ajan maliyeti — CV 0.58.

**Gözlenen ilerleme.** Yorumcu ve bağlı PR yok.

## 8. [#12255](https://github.com/can1357/oh-my-pi/issues/12255) — architect JSON fence regex

**Skor:** 0.68 / 0.60 / easy 0.94 · gözlenen aktif katkıcı 0 · gözlenen açık PR yok.

**Neden.** `n6a()` iç fence’i yakalıyor, `JSON.parse` patlıyor. Ham metin aslında geçerli JSON. Üç kayıtlı session ile doğrulanmış.

**Confidence.** Tek regex, repro tablosu var. Agent-hub TypeScript. CV 0.60.

**Gözlenen ilerleme.** Yorumcu ve bağlı PR yok. Taze issue (etiketsiz); yarış yok.

## 9. [#11605](https://github.com/can1357/oh-my-pi/issues/11605) — Collab Web dosya/medya upload

**Skor:** 0.55 / **0.62** / mid 0.98 · gözlenen aktif katkıcı 0 · gözlenen açık PR yok.

**Neden.** `packages/collab-web` composer’da dosya seçici yok; mobil galeri/kamera ve log/json. Image zaten `CollabFrame.images`.

**Confidence.** Mid: web client + frame protokolü. Diff conf 0.98. CV 0.62: resume React/Tailwind. Beginner 0.55 sınırda — UI yüzeyi biraz geniş.

**Gözlenen ilerleme.** Yorumcu ve bağlı PR yok.

## 10. [#8729](https://github.com/can1357/oh-my-pi/issues/8729) — Biome format vs check

**Skor:** 0.68 / 0.54 / easy 0.95 · gözlenen aktif katkıcı 0 · gözlenen açık PR yok.

**Neden.** `BiomeClient.format()` `biome format --write` çağırıyor; assist/safe-fix `biome check --write`’ta. Repro komutları issue’da.

**Confidence.** Bir argv değişimi + test. LSP/tooling, TypeScript.

**Gözlenen ilerleme.** Yorumcu ve bağlı PR yok.

## 11. [#6094](https://github.com/can1357/oh-my-pi/issues/6094) — para birimi sembolü

**Skor:** 0.57 / 0.56 / mid 0.97 · gözlenen aktif katkıcı 0 · gözlenen açık PR yok.

**Neden.** Maliyet sayısı `models.yml` ile değişiyor, prefix hâlâ `$`. `display.currencySymbol`.

**Confidence.** Mid: birkaç render noktası. Conf 0.97. CV: CLI/TUI ayarı.

**Gözlenen ilerleme.** Yorumcu ve bağlı PR yok.

## 12. [#11096](https://github.com/can1357/oh-my-pi/issues/11096) — `browser-relay status`

**Skor:** 0.60 / 0.55 / mid 0.95 · gözlenen aktif katkıcı 0 · gözlenen açık PR yok.

**Neden.** CLI yalnız `serve|install`. Relay ayakta ama extension bağlı değilken teşhis yok.

**Confidence.** Yeni altkomut, mevcut relay state. Resume CLI/Linux. Mid çünkü birkaç durum biti.

**Gözlenen ilerleme.** Yorumcu ve bağlı PR yok.

## 13. [#7052](https://github.com/can1357/oh-my-pi/issues/7052) — stats CSV/Excel

**Skor:** 0.61 / 0.62 / mid 0.87 · gözlenen aktif katkıcı 0 · gözlenen açık PR yok.

**Neden.** `omp stats` web sayfasından token satırlarını filtreleyip CSV. Resume’da Pandas/maliyet takibi var.

**Confidence.** Mid: tablo + UI. Conf 0.87. CV 0.62 güçlü.

**Gözlenen ilerleme.** Yorumcu ve bağlı PR yok. Aynı yazarın [#7076](https://github.com/can1357/oh-my-pi/issues/7076) ile küçük stats paketi yapılabilir.

## 14. [#7076](https://github.com/can1357/oh-my-pi/issues/7076) — `omp stats --no-open`

**Skor:** 0.78 / 0.56 / easy 0.81 · gözlenen aktif katkıcı 0 · gözlenen açık PR yok.

**Neden.** Dashboard her seferinde tarayıcı açıyor; WSL/headless için `--no-open`. `--summary`/`--json` sunucuyu ayakta tutmuyor.

**Confidence.** Klasik CLI flag. Beginner 0.78. Diff conf 0.81 (opener kodu nerede biraz belirsiz) ama iş dar.

**Gözlenen ilerleme.** Yorumcu ve bağlı PR yok. 7052’den daha iyi ilk PR.

## 15. [#11145](https://github.com/can1357/oh-my-pi/issues/11145) — Ask Submit tab notu

**Skor:** 0.62 / 0.55 / mid 0.89 · gözlenen aktif katkıcı 0 · gözlenen açık PR yok.

**Neden.** Çoklu soruda son Submit yalnız Enter; `n` notu soru tab’ında ve seçim değişince düşüyor.

**Confidence.** Handler isimleri issue’da. Mid. Resume TUI.

**Gözlenen ilerleme.** Yorumcu ve bağlı PR yok. [#10943](https://github.com/can1357/oh-my-pi/issues/10943) ile aynı `n note` kalıbı.

## 16. [#5346](https://github.com/can1357/oh-my-pi/issues/5346) — kullanıcı mesajına datetime

**Skor:** 0.82 / 0.54 / easy 0.79 · gözlenen aktif katkıcı 0 · gözlenen açık PR yok.

**Neden.** Transcript’te “ne zaman yazdım” yok. Format örneği var.

**Confidence.** Beginner 0.82: görüntü. Diff conf 0.79 (timezone/export belirsiz). CV zayıf-orta (saf UX).

**Gözlenen ilerleme.** Yorumcu ve bağlı PR yok.

## 17. [#10943](https://github.com/can1357/oh-my-pi/issues/10943) — `/review` predefined note

**Skor:** 0.63 / 0.54 / mid 0.89 · gözlenen aktif katkıcı 0 · gözlenen açık PR yok.

**Neden.** Ask’teki `n note`yi `/review` menüsüne; custom instructions base-branch workflow’unu bozuyor.

**Confidence.** Mevcut etkileşimi kopyalamak. 11145 ile paylaşılmış UX.

**Gözlenen ilerleme.** Yorumcu ve bağlı PR yok.

## 18. [#5674](https://github.com/can1357/oh-my-pi/issues/5674) — vibe `fast`/`good` config

**Skor:** 0.66 / 0.55 / mid 0.85 · gözlenen aktif katkıcı 0 · gözlenen açık PR yok.

**Neden.** `fast→sonic→@smol`, `good→task→@task` kullanıcıya görünmüyor. `vibe.fast` / `modelRoles.fast` önerisi.

**Confidence.** Config + agent rolleri. Mid, conf 0.85: dokümantasyon vs gerçek anahtar biraz açık.

**Gözlenen ilerleme.** Yorumcu ve bağlı PR yok.

## 19. [#10887](https://github.com/can1357/oh-my-pi/issues/10887) — truncation notice sayaçları

**Skor:** 0.75 / 0.54 / easy 0.80 · gözlenen aktif katkıcı 0 · gözlenen açık PR yok.

**Neden.** `columnTruncatedLines` / `columnDroppedBytes` `dump()`’ta var; kullanıcı notice’ı yalnız cap yazıyor.

**Confidence.** Alanlar mevcut, format string. Easy, beginner 0.75.

**Gözlenen ilerleme.** Yorumcu ve bağlı PR yok.

## 20. [#4807](https://github.com/can1357/oh-my-pi/issues/4807) — iç URL şemalarını vurgula

**Skor:** 0.60 / 0.55 / mid 0.87 · gözlenen aktif katkıcı 0 · gözlenen açık PR yok.

**Neden.** `skill://`, `local://`, `memory://` vb. sohbet markdown’ında düz metin. Hex swatch ve link teması zaten `packages/tui/src/components/markdown.ts` içinde; aynı kalıba scheme token’ı.

**Confidence.** Mid: renderer + theme. Diff conf 0.87. CV TUI/TypeScript. Beginner 0.60. Yazar ilerleme beyanı yok.

**Gözlenen ilerleme.** Yorumcu ve bağlı PR yok.

---

## Bilerek dışarıda bırakılanlar

- **[#4993](https://github.com/can1357/oh-my-pi/issues/4993)** — beginner+CV kesişiminde, açık PR yok, yorumcu yok; **ama** yazar gövdede “I have a working implementation with tests ready. I would love to contribute it as a PR” diyor. Yalnız issue açmak sayılmaz; bu beyan gözlenen katkıcı = 1 / hazır-implementasyon cezası. Rakipsiz değil.
- **Açık PR’li kesişim (46 issue)** — örnek: [#9654](https://github.com/can1357/oh-my-pi/issues/9654) vibe keybinding ([#9866](https://github.com/can1357/oh-my-pi/pull/9866)), [#3760](https://github.com/can1357/oh-my-pi/issues/3760) nested isolation ([#7560](https://github.com/can1357/oh-my-pi/pull/7560)), [#12257](https://github.com/can1357/oh-my-pi/issues/12257) handoff ([#12394](https://github.com/can1357/oh-my-pi/pull/12394)), [#4722](https://github.com/can1357/oh-my-pi/issues/4722) Gemini default ([#9560](https://github.com/can1357/oh-my-pi/pull/9560)). Skor yüksek olsa da yarış var.
- **Provider ekleme** ([#2674](https://github.com/can1357/oh-my-pi/issues/2674) TinyFish vb.) — beginner+CV yüksek; TinyFish için merge [#3572](https://github.com/can1357/oh-my-pi/pull/3572) geçmişi var.
- **[#11815](https://github.com/can1357/oh-my-pi/issues/11815)** — CV noul 0.50 tam eşik.
- Hard issue’lar beginner=hayır; kesişime girmiyor.

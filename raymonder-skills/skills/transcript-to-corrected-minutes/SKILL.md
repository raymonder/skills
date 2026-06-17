---
name: transcript-to-corrected-minutes
description: Use when turning a raw machine transcript, recording transcript, meeting transcript, Plaud transcript, ASR text, or messy bilingual Cantonese/Mandarin transcript into a corrected meeting transcript, minutes-style transcript, or polished transcript with uncertain terms marked.
---

# Transcript To Corrected Minutes

## Overview

Use this skill to convert an initial machine transcript into a corrected, readable meeting transcript while preserving meaning, timing, speaker flow, and uncertainty. If only text is available, call the result a "重校版", "校订版", or "整理版"; do not claim it was re-transcribed from audio.

## Boundary Check

Before editing, determine source availability:

- **Text only**: Work from the transcript. State that no audio was replayed and uncertain parts are inferred from context.
- **Audio or video also provided**: Re-transcribe or spot-check against the media if requested, then note that audio was used.
- **User says to use text after initially mentioning audio**: Follow the latest instruction and proceed text-only.

Do not invent certainty. If a name, organization, product, system, or technical term cannot be reliably recovered, keep it as `[待确认]`.

## Workflow

1. Inspect the source transcript: length, language mix, speaker labels, timestamps, repeated glitches, and obvious ASR error patterns.
2. Identify domain vocabulary from context: organizations, programs, product names, software terms, payment terms, fundraising terms, and names.
3. Build an uncertainty list before or during editing. Include timestamp, suspicious original wording when helpful, and the best current guess.
4. Rewrite into a corrected transcript:
   - Preserve main timestamps and speaker order.
   - Keep useful spoken detail, but remove meaningless filler, accidental repetitions, and stutter loops.
   - Convert obvious ASR errors to the likely intended term when context is strong.
   - Keep bilingual terms where natural, such as `EDM`, `payment gateway`, `tailor-made`, `SPSS`, `SEO`, `API`, `MBTI/INFP`.
   - Use `[待确认]` inline for uncertain names, systems, organizations, amounts, or phrases.
5. Add a short front note explaining the source and limits.
6. Put the concentrated `待确认点` near the top so the user can review efficiently.
7. Generate the requested output format. If the user asks for a document and DOCX tooling is available, create a `.docx`; a Markdown or text copy is also useful for later revision.
8. Verify the output: open/render DOCX when possible, check first and last pages, and scan for leftover template markers, excessive Markdown syntax, or unmarked uncertainty.

## Editing Rules

- Preserve original intent over literal broken wording.
- Do not summarize away substantive discussion unless the user asks for a summary instead of transcript.
- Keep speaker names if known; keep `Speaker 1`, `Speaker 2` when identities are unknown.
- Merge adjacent utterances only when the original transcript clearly split one continuous thought incorrectly.
- Keep timestamps at section starts or individual turns depending on the source density. For long meetings, section ranges plus turn timestamps are usually readable.
- Use Traditional or Simplified Chinese according to the source/user preference. If mixed, default to the user's current language style.
- Use English technical terms where the meeting likely used English; avoid forced Chinese translations for industry terms.
- Never silently convert a low-confidence guess into a definitive statement.

## Common ASR Corrections

Use context, not blind replacement:

| Misrecognized pattern | Likely correction |
|---|---|
| "跳轮妹", "挑了妹", "特拉美" | `tailor-made` |
| "payment giveaway" | `payment gateway` |
| "ICU" in website ranking context | `SEO` |
| "INFT", "NFT" in personality context | `MBTI`, `INFP`, or `[待确认]` |
| "PPIF" near receipts | `PDF` |
| "ATM" near email marketing | `EDM` |
| "MaskCard" | `Mastercard` |
| "前方/QFP" near POS payments | `QFPay` or `[待确认]` |
| "储粮/出粮" in Hong Kong payroll context | `出粮/payroll` |

## Output Template

```markdown
# <meeting title>（重校版文字稿）

整理日期：YYYY-MM-DD

来源：根据现有转写文字重新校对、整理；未回听原始音频。

## 整理说明

本稿基于已有转写文字进行二次校对，重点处理明显的语音识别错误、英文术语误识别、粤语口语被误转为普通话词的问题。由于没有原始音频可供回听，本文不是声学意义上的“重新识别”。无法仅凭上下文可靠判断的内容，以 `[待确认]` 标注。

## 待确认点

- HH:MM:SS <uncertain item and why>

## 重校版文字稿

### HH:MM:SS-HH:MM:SS <section topic>

**HH:MM:SS Speaker：** Corrected transcript text.
```

## Final Response Checklist

When done, tell the user:

- where the corrected document was saved;
- whether audio was or was not used;
- what verification was performed;
- that uncertain points are listed at the top of the document.

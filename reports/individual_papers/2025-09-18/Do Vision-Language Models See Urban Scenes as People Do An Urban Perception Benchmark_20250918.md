# Do Vision-Language Models See Urban Scenes as People Do? An Urban Perception Benchmark

**Korean Title:** 비전-언어 모델은 도시 장면을 사람처럼 인식하는가? 도시 인식 벤치마크

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[authors/Rashid Mushkani|Rashid Mushkani]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Participatory Urban Analysis

## 🔗 유사한 논문
- [[From Pixels to Urban Policy-Intelligence_ Recovering Legacy Effects of Redlining with a Multimodal LLM_20250919|From Pixels to Urban Policy-Intelligence Recovering Legacy Effects of Redlining with a Multimodal LLM]] (83.0% similar)
- [[The Art of Saying Maybe_ A Conformal Lens for Uncertainty Benchmarking in VLMs_20250918|The Art of Saying Maybe A Conformal Lens for Uncertainty Benchmarking in VLMs]] (79.6% similar)
- [[Rationality Check! Benchmarking the Rationality of Large Language Models_20250919|Rationality Check! Benchmarking the Rationality of Large Language Models]] (79.3% similar)
- [[MINGLE_ VLMs for Semantically Complex Region Detection in Urban Scenes_20250918|MINGLE VLMs for Semantically Complex Region Detection in Urban Scenes]] (79.1% similar)
- [[V-SEAM_ Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models_20250919|V-SEAM Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models]] (78.9% similar)

## 📋 저자 정보

**Authors:** Rashid Mushkani

## 📄 Abstract (원문)

Understanding how people read city scenes can inform design and planning. We
introduce a small benchmark for testing vision-language models (VLMs) on urban
perception using 100 Montreal street images, evenly split between photographs
and photorealistic synthetic scenes. Twelve participants from seven community
groups supplied 230 annotation forms across 30 dimensions mixing physical
attributes and subjective impressions. French responses were normalized to
English. We evaluated seven VLMs in a zero-shot setup with a structured prompt
and deterministic parser. We use accuracy for single-choice items and Jaccard
overlap for multi-label items; human agreement uses Krippendorff's alpha and
pairwise Jaccard. Results suggest stronger model alignment on visible,
objective properties than subjective appraisals. The top system (claude-sonnet)
reaches macro 0.31 and mean Jaccard 0.48 on multi-label items. Higher human
agreement coincides with better model scores. Synthetic images slightly lower
scores. We release the benchmark, prompts, and harness for reproducible,
uncertainty-aware evaluation in participatory urban analysis.

## 🔍 Abstract (한글 번역)

도시 장면을 사람들이 어떻게 읽는지를 이해하는 것은 설계와 계획에 정보를 제공할 수 있습니다. 우리는 도시 인식을 테스트하기 위해 100개의 몬트리올 거리 이미지를 사용하여 사진과 사실적인 합성 장면을 균등하게 나눈 소규모 벤치마크를 소개합니다. 7개의 커뮤니티 그룹에서 온 12명의 참가자가 물리적 속성과 주관적 인상을 혼합한 30개 차원에 걸쳐 230개의 주석 양식을 제공했습니다. 프랑스어 응답은 영어로 표준화되었습니다. 우리는 구조화된 프롬프트와 결정론적 파서를 사용하여 제로샷 설정에서 7개의 비전-언어 모델(VLM)을 평가했습니다. 단일 선택 항목에는 정확도를 사용하고, 다중 레이블 항목에는 자카드 중첩을 사용합니다. 인간의 합의는 Krippendorff의 알파와 쌍별 자카드를 사용합니다. 결과는 주관적 평가보다 가시적이고 객관적인 속성에서 모델 정렬이 더 강하다는 것을 시사합니다. 최고 시스템(claude-sonnet)은 다중 레이블 항목에서 매크로 0.31과 평균 자카드 0.48에 도달합니다. 인간의 합의가 높을수록 모델 점수가 더 좋습니다. 합성 이미지는 점수를 약간 낮춥니다. 우리는 참여적 도시 분석에서 재현 가능하고 불확실성을 인식하는 평가를 위해 벤치마크, 프롬프트 및 하네스를 공개합니다.

## 📝 요약

이 논문은 도시 장면을 읽는 방법을 이해하여 디자인과 계획에 활용할 수 있는 연구를 소개합니다. 몬트리올 거리 이미지 100장을 사용하여 시각-언어 모델(VLMs)을 테스트하는 작은 벤치마크를 제안했습니다. 7개 커뮤니티 그룹의 12명의 참가자가 30개 차원에서 물리적 속성과 주관적 인상을 혼합한 230개의 주석 양식을 제공했습니다. 7개의 VLMs를 제로샷 설정으로 평가했으며, 결과는 가시적이고 객관적인 속성에서 모델의 일치도가 더 높음을 시사합니다. 최고 성능을 보인 시스템은 다중 레이블 항목에서 매크로 0.31과 평균 자카드 0.48을 기록했습니다. 인간의 합의도가 높은 경우 모델 점수도 향상되었습니다. 인공 이미지는 점수를 약간 낮췄습니다. 이 연구는 벤치마크, 프롬프트 및 평가 도구를 공개하여 참여형 도시 분석에서 재현 가능하고 불확실성을 고려한 평가를 가능하게 합니다.

## 🎯 주요 포인트

- 1. 도시 장면을 읽는 방법에 대한 이해는 디자인과 계획에 유용한 정보를 제공할 수 있습니다.

- 2. 몬트리올 거리 이미지 100장을 사용하여 도시 인식을 테스트하는 비전-언어 모델(VLMs) 벤치마크를 소개합니다.

- 3. 7개의 커뮤니티 그룹에서 12명의 참가자가 30가지 차원에 걸쳐 230개의 주석 양식을 제공하였습니다.

- 4. 연구 결과, 모델은 가시적이고 객관적인 속성에 대해 더 강한 일치를 보였으며, 주관적인 평가에서는 약한 일치를 보였습니다.

- 5. 벤치마크, 프롬프트 및 평가 도구를 공개하여 참여형 도시 분석에서 재현 가능하고 불확실성을 고려한 평가를 지원합니다.

---

*Generated on 2025-09-20 05:51:28*
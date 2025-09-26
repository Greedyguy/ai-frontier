---
keywords:
  - Edit Distance
  - Hamming Distance
  - Wildcard Matching
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14898
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:23:20.905599",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Edit Distance",
    "Hamming Distance",
    "Wildcard Matching"
  ],
  "rejected_keywords": [
    "Streaming Algorithms",
    "Grammar Decomposition"
  ],
  "similarity_scores": {
    "Edit Distance": 0.8,
    "Hamming Distance": 0.78,
    "Wildcard Matching": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Streaming periodicity with mismatches, wildcards, and edits

**Korean Title:** 불일치, 와일드카드, 편집이 있는 스트리밍 주기성

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Edit Distance|edit distance]], [[keywords/Hamming Distance|Hamming distance]]
**⚡ Unique Technical**: [[keywords/Wildcard Matching|wildcards]]

## 🔗 유사한 논문
- [[Accelerated Gradient Methods with Biased Gradient Estimates Risk Sensitivity, High-Probability Guarantees, and Large Deviation Bounds]] (74.0% similar)
- [[Moment- and Power-Spectrum-Based Gaussianity Regularization for Text-to-Image Models_20250919|Moment- and Power-Spectrum-Based Gaussianity Regularization for Text-to-Image Models]] (73.4% similar)
- [[Multimodal Hate Detection Using Dual-Stream Graph Neural Networks]] (73.1% similar)
- [[Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning_20250918|Data-Driven Distributed Optimization via Aggregative Tracking and Deep-Learning]] (73.1% similar)
- [[Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production_20250919|Hybrid Autoregressive-Diffusion Model for Real-Time Sign Language Production]] (73.0% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14898v1 Announce Type: new 
Abstract: In this work, we study the problem of detecting periodic trends in strings. While detecting exact periodicity has been studied extensively, real-world data is often noisy, where small deviations or mismatches occur between repetitions. This work focuses on a generalized approach to period detection that efficiently handles noise. Given a string $S$ of length $n$, the task is to identify integers $p$ such that the prefix and the suffix of $S$, each of length $n-p+1$, are similar under a given distance measure. Erg\"un et al. [APPROX-RANDOM 2017] were the first to study this problem in the streaming model under the Hamming distance. In this work, we combine, in a non-trivial way, the Hamming distance sketch of Clifford et al. [SODA 2019] and the structural description of the $k$-mismatch occurrences of a pattern in a text by Charalampopoulos et al. [FOCS 2020] to present a more efficient streaming algorithm for period detection under the Hamming distance. As a corollary, we derive a streaming algorithm for detecting periods of strings which may contain wildcards, a special symbol that match any character of the alphabet. Our algorithm is not only more efficient than that of Erg\"un et al. [TCS 2020], but it also operates without their assumption that the string must be free of wildcards in its final characters. Additionally, we introduce the first two-pass streaming algorithm for computing periods under the edit distance by leveraging and extending the Bhattacharya-Kouck\'y's grammar decomposition technique [STOC 2023].

## 🔍 Abstract (한글 번역)

arXiv:2509.14898v1 발표 유형: 신규  
초록: 본 연구에서는 문자열에서 주기적 경향을 탐지하는 문제를 연구합니다. 정확한 주기성을 탐지하는 문제는 광범위하게 연구되었지만, 실제 데이터는 종종 반복 사이에 작은 편차나 불일치가 발생하는 노이즈가 존재합니다. 본 연구는 노이즈를 효율적으로 처리할 수 있는 주기 탐지의 일반화된 접근법에 중점을 둡니다. 길이가 $n$인 문자열 $S$가 주어졌을 때, 접두사와 접미사 각각의 길이가 $n-p+1$인 부분이 주어진 거리 측정 기준에 따라 유사한 정수 $p$를 식별하는 것이 과제입니다. Ergün 등 [APPROX-RANDOM 2017]은 해밍 거리 하에서 스트리밍 모델로 이 문제를 처음 연구했습니다. 본 연구에서는 Clifford 등 [SODA 2019]의 해밍 거리 스케치와 Charalampopoulos 등 [FOCS 2020]의 텍스트에서 패턴의 $k$-불일치 발생에 대한 구조적 설명을 비트리비얼하게 결합하여 해밍 거리 하에서 주기 탐지를 위한 보다 효율적인 스트리밍 알고리즘을 제시합니다. 결과적으로, 알파벳의 모든 문자와 일치할 수 있는 특수 기호인 와일드카드를 포함할 수 있는 문자열의 주기를 탐지하는 스트리밍 알고리즘을 도출합니다. 우리의 알고리즘은 Ergün 등 [TCS 2020]의 알고리즘보다 더 효율적일 뿐만 아니라, 문자열의 마지막 문자에 와일드카드가 없어야 한다는 가정 없이 작동합니다. 추가적으로, Bhattacharya-Koucký의 문법 분해 기법 [STOC 2023]을 활용하고 확장하여 편집 거리 하에서 주기를 계산하는 최초의 두 번의 패스 스트리밍 알고리즘을 소개합니다.

## 📝 요약

이 연구는 문자열에서 주기적 경향을 탐지하는 문제를 다룹니다. 기존 연구는 정확한 주기 탐지에 집중했지만, 실제 데이터는 노이즈가 있어 반복 간의 작은 차이가 발생합니다. 본 연구는 이러한 노이즈를 효율적으로 처리하는 일반화된 주기 탐지 방법을 제시합니다. 주어진 문자열의 접두사와 접미사가 특정 거리 측정 기준 하에 유사한 정수 $p$를 식별하는 것이 목표입니다. 본 연구는 Hamming 거리 기반의 스트리밍 알고리즘을 개발하여 Ergün 등의 기존 방법보다 효율적이며, 와일드카드를 포함한 문자열의 주기도 탐지할 수 있습니다. 또한, Bhattacharya-Koucký의 문법 분해 기법을 확장하여 편집 거리 기반의 이중 패스 스트리밍 알고리즘도 처음으로 도입했습니다.

## 🎯 주요 포인트

- 1. 본 연구는 문자열에서 주기적 경향을 탐지하는 문제를 다루며, 특히 노이즈가 있는 실제 데이터에 대한 일반화된 접근 방식을 제안합니다.

- 2. Hamming 거리 하에서 주기 탐지를 위한 보다 효율적인 스트리밍 알고리즘을 제시하며, 이는 Clifford et al.의 Hamming 거리 스케치와 Charalampopoulos et al.의 $k$-mismatch 구조를 결합한 것입니다.

- 3. 와일드카드를 포함할 수 있는 문자열의 주기를 탐지하는 스트리밍 알고리즘을 도출하였으며, 이는 Erg\"un et al.의 알고리즘보다 효율적이고 와일드카드가 없는 최종 문자에 대한 가정 없이 작동합니다.

- 4. Bhattacharya-Kouck\'y's 문법 분해 기법을 확장하여 편집 거리 하에서 주기를 계산하는 최초의 두 번 통과 스트리밍 알고리즘을 소개합니다.

---

*Generated on 2025-09-19 16:24:28*
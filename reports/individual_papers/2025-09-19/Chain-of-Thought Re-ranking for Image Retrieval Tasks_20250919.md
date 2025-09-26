---
keywords:
  - Text-to-Image Retrieval
  - Large Language Models
  - Composed Image Retrieval
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14746
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:53:21.572684",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Text-to-Image Retrieval",
    "Large Language Models",
    "Composed Image Retrieval"
  ],
  "rejected_keywords": [
    "Chain-of-Thought Re-Ranking",
    "Image Retrieval"
  ],
  "similarity_scores": {
    "Text-to-Image Retrieval": 0.8,
    "Large Language Models": 0.78,
    "Composed Image Retrieval": 0.79
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Chain-of-Thought Re-ranking for Image Retrieval Tasks

**Korean Title:** 이미지 검색 작업을 위한 사고의 연쇄 재정렬

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Text-to-Image Retrieval|Text-to-Image Retrieval]], [[keywords/Composed Image Retrieval|Composed Image Retrieval]]
**🚀 Evolved Concepts**: [[keywords/Large Language Models|Multimodal Large Language Models]]

## 🔗 유사한 논문
- [[Uni-cot Towards Unified Chain-of-Thought Reasoning Across Text and Vision]] (83.5% similar)
- [[MARIC Multi-Agent Reasoning for Image Classification]] (82.3% similar)
- [[MAgICoRe Multi-Agent, Iterative, Coarse-to-Fine Refinement for Reasoning]] (81.4% similar)
- [[Reasoning Efficiently Through Adaptive Chain-of-Thought Compression A Self-Optimizing Framework]] (81.0% similar)
- [[WebCoT Enhancing Web Agent Reasoning by Reconstructing Chain-of-Thought in Reflection, Branching, and Rollback]] (80.8% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14746v1 Announce Type: new 
Abstract: Image retrieval remains a fundamental yet challenging problem in computer vision. While recent advances in Multimodal Large Language Models (MLLMs) have demonstrated strong reasoning capabilities, existing methods typically employ them only for evaluation, without involving them directly in the ranking process. As a result, their rich multimodal reasoning abilities remain underutilized, leading to suboptimal performance. In this paper, we propose a novel Chain-of-Thought Re-Ranking (CoTRR) method to address this issue. Specifically, we design a listwise ranking prompt that enables MLLM to directly participate in re-ranking candidate images. This ranking process is grounded in an image evaluation prompt, which assesses how well each candidate aligns with users query. By allowing MLLM to perform listwise reasoning, our method supports global comparison, consistent reasoning, and interpretable decision-making - all of which are essential for accurate image retrieval. To enable structured and fine-grained analysis, we further introduce a query deconstruction prompt, which breaks down the original query into multiple semantic components. Extensive experiments on five datasets demonstrate the effectiveness of our CoTRR method, which achieves state-of-the-art performance across three image retrieval tasks, including text-to-image retrieval (TIR), composed image retrieval (CIR) and chat-based image retrieval (Chat-IR). Our code is available at https://github.com/freshfish15/CoTRR .

## 🔍 Abstract (한글 번역)

arXiv:2509.14746v1 발표 유형: 신규  
초록: 이미지 검색은 컴퓨터 비전 분야에서 여전히 기본적이면서도 도전적인 문제로 남아 있습니다. 최근 다중모달 대형 언어 모델(Multimodal Large Language Models, MLLMs)의 발전은 강력한 추론 능력을 보여주었지만, 기존 방법들은 주로 평가에만 이를 활용하고, 순위 결정 과정에 직접적으로 관여시키지 않습니다. 그 결과, MLLM의 풍부한 다중모달 추론 능력이 충분히 활용되지 않아 최적의 성능을 발휘하지 못하고 있습니다. 본 논문에서는 이러한 문제를 해결하기 위해 새로운 사고의 사슬 재순위(Chain-of-Thought Re-Ranking, CoTRR) 방법을 제안합니다. 구체적으로, MLLM이 후보 이미지의 재순위에 직접 참여할 수 있도록 하는 리스트 방식의 순위 매김 프롬프트를 설계했습니다. 이 순위 매김 과정은 각 후보가 사용자 쿼리와 얼마나 잘 일치하는지를 평가하는 이미지 평가 프롬프트에 기반을 두고 있습니다. MLLM이 리스트 방식의 추론을 수행할 수 있도록 함으로써, 본 방법은 전역 비교, 일관된 추론, 해석 가능한 의사결정을 지원하며, 이는 정확한 이미지 검색에 필수적입니다. 구조적이고 세밀한 분석을 가능하게 하기 위해, 원래의 쿼리를 여러 의미적 구성 요소로 분해하는 쿼리 분해 프롬프트도 도입했습니다. 다섯 개의 데이터셋에 대한 광범위한 실험을 통해, 본 CoTRR 방법이 텍스트-이미지 검색(TIR), 구성 이미지 검색(CIR), 채팅 기반 이미지 검색(Chat-IR)을 포함한 세 가지 이미지 검색 작업에서 최첨단 성능을 달성함을 입증했습니다. 우리의 코드는 https://github.com/freshfish15/CoTRR 에서 확인할 수 있습니다.

## 📝 요약

이 논문은 이미지 검색의 성능을 향상시키기 위해 새로운 체인 오브 쏘트 재랭킹(CoTRR) 방법을 제안합니다. 기존의 다중모달 대형 언어 모델(MLLM)은 주로 평가에만 사용되었으나, CoTRR은 MLLM을 직접 재랭킹 과정에 참여시켜 그들의 다중모달 추론 능력을 활용합니다. 이를 위해 리스트형 랭킹 프롬프트를 설계하여 MLLM이 후보 이미지들을 전역적으로 비교하고 일관된 추론과 해석 가능한 의사결정을 수행할 수 있도록 합니다. 또한, 쿼리 분해 프롬프트를 도입하여 쿼리를 여러 의미 구성 요소로 나누어 세밀한 분석을 지원합니다. 실험 결과, CoTRR은 텍스트-이미지 검색, 구성 이미지 검색, 채팅 기반 이미지 검색 등 세 가지 이미지 검색 작업에서 최첨단 성능을 달성했습니다.

## 🎯 주요 포인트

- 1. 본 논문은 이미지 검색 문제에서 멀티모달 대형 언어 모델(MLLM)의 활용을 제안하며, 기존 방법의 한계를 극복하기 위해 Chain-of-Thought Re-Ranking (CoTRR) 방법을 제안합니다.

- 2. CoTRR 방법은 MLLM이 후보 이미지의 재정렬 과정에 직접 참여하도록 하여, 글로벌 비교와 일관된 추론, 해석 가능한 의사결정을 지원합니다.

- 3. 쿼리 분해 프롬프트를 도입하여 원래의 쿼리를 여러 의미 구성 요소로 분해함으로써 구조적이고 세밀한 분석을 가능하게 합니다.

- 4. 다섯 개의 데이터셋에 대한 실험 결과, CoTRR 방법은 텍스트-이미지 검색, 구성 이미지 검색, 채팅 기반 이미지 검색 등 세 가지 이미지 검색 작업에서 최첨단 성능을 달성했습니다.

- 5. 연구 결과의 재현성을 위해 코드가 공개되어 있습니다: https://github.com/freshfish15/CoTRR.

---

*Generated on 2025-09-19 16:06:01*
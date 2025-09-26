---
keywords:
  - Open-Vocabulary Semantic Segmentation
  - Vocabulary Alignment
  - Vision Transformers
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:21:14.036664",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Open-Vocabulary Semantic Segmentation",
    "Vocabulary Alignment",
    "Vision Transformers"
  ],
  "rejected_keywords": [
    "Source-Free Domain Adaptation",
    "Low-Rank Adaptation"
  ],
  "similarity_scores": {
    "Open-Vocabulary Semantic Segmentation": 0.82,
    "Vocabulary Alignment": 0.85,
    "Vision Transformers": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Lost in Translation? Vocabulary Alignment for Source-Free Domain Adaptation in Open-Vocabulary Semantic Segmentation

**Korean Title:** 번역에서 길을 잃다? 개방형 어휘 의미 분할에서 소스 없는 도메인 적응을 위한 어휘 정렬

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Vision Transformers|Vision Transformers]]
**⚡ Unique Technical**: [[keywords/Open-Vocabulary Semantic Segmentation|Open-Vocabulary Semantic Segmentation]], [[keywords/Vocabulary Alignment|Vocabulary Alignment]]

## 🔗 유사한 논문
- [[GeoAware-VLA_ Implicit Geometry Aware Vision-Language-Action Model_20250918|GeoAware-VLA Implicit Geometry Aware Vision-Language-Action Model]] (82.3% similar)
- [[ForceVLA_ Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation_20250919|ForceVLA Enhancing VLA Models with a Force-aware MoE for Contact-rich Manipulation]] (80.9% similar)
- [[Middo_ Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning_20250919|Middo Model-Informed Dynamic Data Optimization for Enhanced LLM Fine-Tuning via Closed-Loop Learning]] (80.7% similar)
- [[V-SEAM_ Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models_20250919|V-SEAM Visual Semantic Editing and Attention Modulating for Causal Interpretability of Vision-Language Models]] (80.6% similar)
- [[UnifiedVisual_ A Framework for Constructing Unified Vision-Language Datasets_20250919|UnifiedVisual A Framework for Constructing Unified Vision-Language Datasets]] (80.4% similar)

## 📋 저자 정보

**Authors:** Silvio Mazzucco, Carl Persson, Mattia Segu, Pier Luigi Dovesi, Federico Tombari, Luc Van Gool, Matteo Poggi

## 📄 Abstract (원문)

We introduce VocAlign, a novel source-free domain adaptation framework
specifically designed for VLMs in open-vocabulary semantic segmentation. Our
method adopts a student-teacher paradigm enhanced with a vocabulary alignment
strategy, which improves pseudo-label generation by incorporating additional
class concepts. To ensure efficiency, we use Low-Rank Adaptation (LoRA) to
fine-tune the model, preserving its original capabilities while minimizing
computational overhead. In addition, we propose a Top-K class selection
mechanism for the student model, which significantly reduces memory
requirements while further improving adaptation performance. Our approach
achieves a notable 6.11 mIoU improvement on the CityScapes dataset and
demonstrates superior performance on zero-shot segmentation benchmarks, setting
a new standard for source-free adaptation in the open-vocabulary setting.

## 🔍 Abstract (한글 번역)

우리는 개방형 어휘 의미 분할에서 VLMs에 특화된 새로운 소스 프리 도메인 적응 프레임워크인 VocAlign을 소개합니다. 우리의 방법은 추가적인 클래스 개념을 통합하여 의사 레이블 생성을 개선하는 어휘 정렬 전략이 강화된 학생-교사 패러다임을 채택합니다. 효율성을 보장하기 위해, 우리는 모델의 원래 기능을 유지하면서 계산 오버헤드를 최소화하기 위해 저랭크 적응(LoRA)을 사용하여 모델을 미세 조정합니다. 또한, 우리는 학생 모델을 위한 Top-K 클래스 선택 메커니즘을 제안하여 메모리 요구 사항을 크게 줄이면서 적응 성능을 더욱 향상시킵니다. 우리의 접근 방식은 CityScapes 데이터셋에서 6.11 mIoU의 주목할 만한 향상을 달성했으며, 제로샷 분할 벤치마크에서 우수한 성능을 보여주며, 개방형 어휘 설정에서 소스 프리 적응의 새로운 표준을 설정합니다.

## 📝 요약

VocAlign은 VLMs의 오픈 보캐뷸러리 의미론적 분할을 위한 새로운 소스 프리 도메인 적응 프레임워크입니다. 학생-교사 패러다임과 어휘 정렬 전략을 채택하여 추가 클래스 개념을 통합함으로써 의사 레이블 생성을 개선합니다. LoRA를 사용하여 모델을 미세 조정하여 원래의 기능을 유지하면서 계산 부담을 최소화합니다. 또한, 학생 모델에 대한 Top-K 클래스 선택 메커니즘을 제안하여 메모리 요구 사항을 줄이면서 적응 성능을 향상시킵니다. 이 접근법은 CityScapes 데이터셋에서 6.11 mIoU 향상을 이루었고, 제로샷 분할 벤치마크에서 우수한 성능을 보여 소스 프리 적응의 새로운 기준을 세웠습니다.

## 🎯 주요 포인트

- 1. VocAlign은 개방형 어휘 의미 분할을 위한 VLM에 특화된 소스 없는 도메인 적응 프레임워크입니다.

- 2. 학생-교사 패러다임과 어휘 정렬 전략을 채택하여 추가 클래스 개념을 포함한 가짜 레이블 생성을 개선합니다.

- 3. Low-Rank Adaptation(LoRA)을 사용하여 모델을 미세 조정함으로써 원래의 기능을 유지하면서 계산 오버헤드를 최소화합니다.

- 4. 학생 모델을 위한 Top-K 클래스 선택 메커니즘을 제안하여 메모리 요구 사항을 크게 줄이고 적응 성능을 향상시킵니다.

- 5. CityScapes 데이터셋에서 6.11 mIoU 향상을 달성하고, 제로샷 분할 벤치마크에서 우수한 성능을 보여줍니다.

---

*Generated on 2025-09-20 00:45:28*
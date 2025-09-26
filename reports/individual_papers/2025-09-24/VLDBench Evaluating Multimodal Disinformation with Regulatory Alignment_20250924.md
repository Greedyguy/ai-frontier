<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:49:23.585806",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "VLDBench",
    "Multimodal Disinformation",
    "Vision-Language Model",
    "AI Governance Framework"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "VLDBench": 0.8,
    "Multimodal Disinformation": 0.85,
    "Vision-Language Model": 0.88,
    "AI Governance Framework": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "VLDBench",
        "canonical": "VLDBench",
        "aliases": [
          "Vision-Language Disinformation Detection Benchmark"
        ],
        "category": "unique_technical",
        "rationale": "VLDBench is a unique benchmark specifically designed for evaluating multimodal disinformation, providing a new resource for AI research.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Multimodal Disinformation",
        "canonical": "Multimodal Disinformation",
        "aliases": [
          "Multimodal Fake News"
        ],
        "category": "specific_connectable",
        "rationale": "Understanding multimodal disinformation is crucial for developing models that can handle complex data types, enhancing connectivity with related research.",
        "novelty_score": 0.7,
        "connectivity_score": 0.85,
        "specificity_score": 0.8,
        "link_intent_score": 0.85
      },
      {
        "surface": "Vision-Language Models",
        "canonical": "Vision-Language Model",
        "aliases": [
          "VLMs"
        ],
        "category": "evolved_concepts",
        "rationale": "Vision-Language Models represent an evolved concept in AI, crucial for linking research on multimodal data processing.",
        "novelty_score": 0.6,
        "connectivity_score": 0.9,
        "specificity_score": 0.75,
        "link_intent_score": 0.88
      },
      {
        "surface": "AI Governance Frameworks",
        "canonical": "AI Governance Framework",
        "aliases": [
          "AI Risk Management"
        ],
        "category": "broad_technical",
        "rationale": "AI Governance Frameworks are essential for aligning AI development with ethical standards, providing a broad technical context.",
        "novelty_score": 0.55,
        "connectivity_score": 0.7,
        "specificity_score": 0.65,
        "link_intent_score": 0.7
      }
    ],
    "ban_list_suggestions": [
      "disinformation",
      "benchmark",
      "text-image pairs"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "VLDBench",
      "resolved_canonical": "VLDBench",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Multimodal Disinformation",
      "resolved_canonical": "Multimodal Disinformation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.85,
        "specificity": 0.8,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Vision-Language Models",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.9,
        "specificity": 0.75,
        "link_intent": 0.88
      }
    },
    {
      "candidate_surface": "AI Governance Frameworks",
      "resolved_canonical": "AI Governance Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.7,
        "specificity": 0.65,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# VLDBench Evaluating Multimodal Disinformation with Regulatory Alignment

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CL|cs.CL]]
**PDF**: [Download](https://arxiv.org/pdf/2502.11361.pdf)
**Category**: cs.CL
**Published**: 2025-09-24
**ArXiv ID**: [2502.11361](https://arxiv.org/abs/2502.11361)

## 🔗 유사한 논문
- [[2025-09-22/VLA-Mark_ A cross modal watermark for large vision-language alignment model_20250922|VLA-Mark: A cross modal watermark for large vision-language alignment model]] (83.3% similar)
- [[2025-09-19/Rationality Check! Benchmarking the Rationality of Large Language Models_20250919|Rationality Check! Benchmarking the Rationality of Large Language Models]] (82.9% similar)
- [[2025-09-24/VIR-Bench_ Evaluating Geospatial and Temporal Understanding of MLLMs via Travel Video Itinerary Reconstruction_20250924|VIR-Bench: Evaluating Geospatial and Temporal Understanding of MLLMs via Travel Video Itinerary Reconstruction]] (82.6% similar)
- [[2025-09-17/VCBench_ Benchmarking LLMs in Venture Capital_20250917|VCBench: Benchmarking LLMs in Venture Capital]] (82.6% similar)
- [[2025-09-23/OpenGVL - Benchmarking Visual Temporal Progress for Data Curation_20250923|OpenGVL - Benchmarking Visual Temporal Progress for Data Curation]] (82.3% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/AI Governance Framework|AI Governance Framework]]
**🔗 Specific Connectable**: [[keywords/Multimodal Disinformation|Multimodal Disinformation]]
**⚡ Unique Technical**: [[keywords/VLDBench|VLDBench]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.11361v4 Announce Type: replace 
Abstract: Detecting disinformation that blends manipulated text and images has become increasingly challenging, as AI tools make synthetic content easy to generate and disseminate. While most existing AI safety benchmarks focus on single modality misinformation (i.e., false content shared without intent to deceive), intentional multimodal disinformation, such as propaganda or conspiracy theories that imitate credible news, remains largely unaddressed. We introduce the Vision-Language Disinformation Detection Benchmark (VLDBench), the first large-scale resource supporting both unimodal (text-only) and multimodal (text + image) disinformation detection. VLDBench comprises approximately 62,000 labeled text-image pairs across 13 categories, curated from 58 news outlets. Using a semi-automated pipeline followed by expert review, 22 domain experts invested over 500 hours to produce high-quality annotations with substantial inter-annotator agreement. Evaluations of state-of-the-art Large Language Models (LLMs) and Vision-Language Models (VLMs) on VLDBench show that incorporating visual cues improves detection accuracy by 5 to 35 percentage points over text-only models. VLDBench provides data and code for evaluation, fine-tuning, and robustness testing to support disinformation analysis. Developed in alignment with AI governance frameworks (e.g., the MIT AI Risk Repository), VLDBench offers a principled foundation for advancing trustworthy disinformation detection in multimodal media.
  Project: https://vectorinstitute.github.io/VLDBench/ Dataset: https://huggingface.co/datasets/vector-institute/VLDBench Code: https://github.com/VectorInstitute/VLDBench

## 📝 요약

이 논문은 조작된 텍스트와 이미지를 결합한 허위 정보를 탐지하기 위한 새로운 벤치마크인 VLDBench를 소개합니다. 이는 텍스트와 이미지가 결합된 멀티모달 허위 정보 탐지를 지원하는 최초의 대규모 자원으로, 13개 카테고리에서 약 62,000개의 라벨링된 텍스트-이미지 쌍을 포함합니다. 22명의 도메인 전문가가 500시간 이상을 투자하여 높은 품질의 주석을 작성했으며, 최신 대형 언어 모델과 비전-언어 모델을 평가한 결과, 시각적 단서를 포함하면 텍스트만 사용하는 모델에 비해 탐지 정확도가 5~35% 포인트 향상되었습니다. VLDBench는 AI 거버넌스 프레임워크에 따라 개발되어 신뢰할 수 있는 멀티모달 미디어 허위 정보 탐지를 위한 기반을 제공합니다.

## 🎯 주요 포인트

- 1. VLDBench는 텍스트와 이미지를 결합한 멀티모달 허위정보 탐지를 지원하는 최초의 대규모 벤치마크입니다.
- 2. 이 벤치마크는 13개 카테고리에서 약 62,000개의 레이블이 지정된 텍스트-이미지 쌍으로 구성되어 있습니다.
- 3. VLDBench는 시각적 단서를 포함할 때 탐지 정확도가 5~35% 포인트 향상된다는 평가 결과를 보여줍니다.
- 4. 이 벤치마크는 AI 거버넌스 프레임워크와의 정렬을 통해 신뢰할 수 있는 허위정보 탐지를 위한 기반을 제공합니다.
- 5. VLDBench는 데이터와 코드를 제공하여 평가, 미세 조정 및 강건성 테스트를 지원합니다.


---

*Generated on 2025-09-24 15:49:23*
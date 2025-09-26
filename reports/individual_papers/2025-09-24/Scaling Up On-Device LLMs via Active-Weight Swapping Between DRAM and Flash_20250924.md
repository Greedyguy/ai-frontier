<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:23:31.806890",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Active Weight DRAM-Flash Swapping",
    "Sparsity-aware Self-distillation",
    "ActiveFlow"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Active Weight DRAM-Flash Swapping": 0.78,
    "Sparsity-aware Self-distillation": 0.72,
    "ActiveFlow": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM",
          "Large Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Central to the paper's focus on scaling model deployment on devices.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Active Weight DRAM-Flash Swapping",
        "canonical": "Active Weight DRAM-Flash Swapping",
        "aliases": [
          "DRAM-Flash Swapping",
          "Active Weight Swapping"
        ],
        "category": "unique_technical",
        "rationale": "A novel technique introduced in the paper for efficient memory usage.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Sparsity-aware Self-distillation",
        "canonical": "Sparsity-aware Self-distillation",
        "aliases": [
          "Self-distillation",
          "Sparsity-aware Distillation"
        ],
        "category": "unique_technical",
        "rationale": "A specific technique that aligns with the paper's focus on model efficiency.",
        "novelty_score": 0.7,
        "connectivity_score": 0.6,
        "specificity_score": 0.75,
        "link_intent_score": 0.72
      },
      {
        "surface": "ActiveFlow",
        "canonical": "ActiveFlow",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "The primary framework introduced in the paper, central to its contributions.",
        "novelty_score": 0.8,
        "connectivity_score": 0.55,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "adaptive DRAM usage",
      "hot weight cache",
      "computation-involved weights"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Active Weight DRAM-Flash Swapping",
      "resolved_canonical": "Active Weight DRAM-Flash Swapping",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Sparsity-aware Self-distillation",
      "resolved_canonical": "Sparsity-aware Self-distillation",
      "decision": "linked",
      "scores": {
        "novelty": 0.7,
        "connectivity": 0.6,
        "specificity": 0.75,
        "link_intent": 0.72
      }
    },
    {
      "candidate_surface": "ActiveFlow",
      "resolved_canonical": "ActiveFlow",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.55,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Scaling Up On-Device LLMs via Active-Weight Swapping Between DRAM and Flash

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2504.08378.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2504.08378](https://arxiv.org/abs/2504.08378)

## 🔗 유사한 논문
- [[2025-09-23/MobiZO_ Enabling Efficient LLM Fine-Tuning at the Edge via Inference Engines_20250923|MobiZO: Enabling Efficient LLM Fine-Tuning at the Edge via Inference Engines]] (85.2% similar)
- [[2025-09-23/70% Size, 100% Accuracy_ Lossless LLM Compression for Efficient GPU Inference via Dynamic-Length Float_20250923|70% Size, 100% Accuracy: Lossless LLM Compression for Efficient GPU Inference via Dynamic-Length Float]] (85.1% similar)
- [[2025-09-18/LLM-I_ LLMs are Naturally Interleaved Multimodal Creators_20250918|LLM-I: LLMs are Naturally Interleaved Multimodal Creators]] (83.2% similar)
- [[2025-09-18/The Energy-Efficient Hierarchical Neural Network with Fast FPGA-Based Incremental Learning_20250918|The Energy-Efficient Hierarchical Neural Network with Fast FPGA-Based Incremental Learning]] (83.0% similar)
- [[2025-09-24/LCMF_ Lightweight Cross-Modality Mambaformer for Embodied Robotics VQA_20250924|LCMF: Lightweight Cross-Modality Mambaformer for Embodied Robotics VQA]] (82.9% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**⚡ Unique Technical**: [[keywords/Active Weight DRAM-Flash Swapping|Active Weight DRAM-Flash Swapping]], [[keywords/Sparsity-aware Self-distillation|Sparsity-aware Self-distillation]], [[keywords/ActiveFlow|ActiveFlow]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2504.08378v2 Announce Type: replace 
Abstract: Large language models (LLMs) are increasingly being deployed on mobile devices, but the limited DRAM capacity constrains the deployable model size. This paper introduces ActiveFlow, the first LLM inference framework that can achieve adaptive DRAM usage for modern LLMs (not ReLU-based), enabling the scaling up of deployable model sizes. The framework is based on the novel concept of active weight DRAM-flash swapping and incorporates three novel techniques: (1) Cross-layer active weights preloading. It uses the activations from the current layer to predict the active weights of several subsequent layers, enabling computation and data loading to overlap, as well as facilitating large I/O transfers. (2) Sparsity-aware self-distillation. It adjusts the active weights to align with the dense-model output distribution, compensating for approximations introduced by contextual sparsity. (3) Active weight DRAM-flash swapping pipeline. It orchestrates the DRAM space allocation among the hot weight cache, preloaded active weights, and computation-involved weights based on available memory. Results show ActiveFlow achieves the performance-cost Pareto frontier compared to existing efficiency optimization methods.

## 📝 요약

이 논문은 모바일 장치에서 대형 언어 모델(LLM)의 배포를 위한 ActiveFlow라는 프레임워크를 소개합니다. ActiveFlow는 DRAM 용량의 제약을 극복하고 배포 가능한 모델 크기를 확장할 수 있도록 적응형 DRAM 사용을 실현합니다. 주요 기여는 다음과 같습니다: (1) Cross-layer active weights preloading 기법을 통해 여러 레이어의 활성 가중치를 예측하여 계산과 데이터 로딩을 중첩시킵니다. (2) Sparsity-aware self-distillation 기법으로 활성 가중치를 조정하여 밀집 모델 출력 분포와 일치시킵니다. (3) Active weight DRAM-flash swapping pipeline을 통해 DRAM 공간을 효율적으로 관리합니다. 실험 결과, ActiveFlow는 기존 최적화 방법과 비교하여 성능-비용의 파레토 최적점을 달성했습니다.

## 🎯 주요 포인트

- 1. ActiveFlow는 현대 LLM의 적응형 DRAM 사용을 가능하게 하여 배포 가능한 모델 크기를 확장할 수 있는 첫 번째 LLM 추론 프레임워크입니다.
- 2. 이 프레임워크는 활성 가중치 DRAM-플래시 스와핑이라는 새로운 개념을 기반으로 하며, 세 가지 혁신적인 기술을 통합합니다.
- 3. 크로스 레이어 활성 가중치 프리로딩은 현재 레이어의 활성화를 사용하여 여러 후속 레이어의 활성 가중치를 예측하여 계산과 데이터 로딩을 겹치게 합니다.
- 4. 희소성 인식 자기 증류는 활성 가중치를 조정하여 밀집 모델 출력 분포에 맞추고, 맥락적 희소성으로 인한 근사치를 보상합니다.
- 5. 활성 가중치 DRAM-플래시 스와핑 파이프라인은 사용 가능한 메모리에 따라 DRAM 공간 할당을 조정하여 성능-비용의 파레토 전선을 달성합니다.


---

*Generated on 2025-09-24 15:23:31*
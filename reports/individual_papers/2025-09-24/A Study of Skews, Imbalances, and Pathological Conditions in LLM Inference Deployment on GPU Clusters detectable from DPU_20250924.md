<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:45:01.963952",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "DPU-assisted Framework",
    "Tensor-parallel Inference",
    "Load Imbalance"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "DPU-assisted Framework": 0.7,
    "Tensor-parallel Inference": 0.82,
    "Load Imbalance": 0.8
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
          "Large Transformer-based Language Models"
        ],
        "category": "broad_technical",
        "rationale": "Connects to the broader field of language model research and applications.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "DPU-assisted framework",
        "canonical": "DPU-assisted Framework",
        "aliases": [
          "Data Processing Unit Framework"
        ],
        "category": "unique_technical",
        "rationale": "Introduces a novel approach for leveraging DPUs in inference tasks, which is specific to this study.",
        "novelty_score": 0.75,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.7
      },
      {
        "surface": "Tensor-parallel inference",
        "canonical": "Tensor-parallel Inference",
        "aliases": [
          "Multi-node Tensor Inference"
        ],
        "category": "specific_connectable",
        "rationale": "Highlights a specific inference strategy relevant to distributed computing environments.",
        "novelty_score": 0.55,
        "connectivity_score": 0.78,
        "specificity_score": 0.72,
        "link_intent_score": 0.82
      },
      {
        "surface": "Load imbalance",
        "canonical": "Load Imbalance",
        "aliases": [
          "Load Skew",
          "Imbalance"
        ],
        "category": "specific_connectable",
        "rationale": "Key issue in distributed computing that affects performance, relevant for optimization studies.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.65,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "runtime efficiency",
      "throughput degradation",
      "latency spikes"
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
      "candidate_surface": "DPU-assisted framework",
      "resolved_canonical": "DPU-assisted Framework",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Tensor-parallel inference",
      "resolved_canonical": "Tensor-parallel Inference",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.78,
        "specificity": 0.72,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Load imbalance",
      "resolved_canonical": "Load Imbalance",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.65,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# A Study of Skews, Imbalances, and Pathological Conditions in LLM Inference Deployment on GPU Clusters detectable from DPU

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18114.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18114](https://arxiv.org/abs/2509.18114)

## 🔗 유사한 논문
- [[2025-09-22/Characterizing the Efficiency of Distributed Training_ A Power, Performance, and Thermal Perspective_20250922|Characterizing the Efficiency of Distributed Training: A Power, Performance, and Thermal Perspective]] (85.4% similar)
- [[2025-09-24/Intra-DP_ A High Performance Collaborative Inference System for Mobile Edge Computing_20250924|Intra-DP: A High Performance Collaborative Inference System for Mobile Edge Computing]] (83.8% similar)
- [[2025-09-23/PDTrim_ Targeted Pruning for Prefill-Decode Disaggregation in Inference_20250923|PDTrim: Targeted Pruning for Prefill-Decode Disaggregation in Inference]] (83.3% similar)
- [[2025-09-23/Robust LLM Training Infrastructure at ByteDance_20250923|Robust LLM Training Infrastructure at ByteDance]] (83.0% similar)
- [[2025-09-23/70% Size, 100% Accuracy_ Lossless LLM Compression for Efficient GPU Inference via Dynamic-Length Float_20250923|70% Size, 100% Accuracy: Lossless LLM Compression for Efficient GPU Inference via Dynamic-Length Float]] (82.8% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Tensor-parallel Inference|Tensor-parallel Inference]], [[keywords/Load Imbalance|Load Imbalance]]
**⚡ Unique Technical**: [[keywords/DPU-assisted Framework|DPU-assisted Framework]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18114v1 Announce Type: new 
Abstract: Autoregressive inference in large transformer-based language models (LLMs) presents significant challenges for runtime efficiency, particularly during the decode phase where load imbalance across GPU shards can cause throughput degradation and latency spikes. A DPU-assisted framework leveraged by BlueField-3 Data Processing Units can enable real-time detection and mitigation of load imbalance in multi-node tensor-parallel inference. By offloading monitoring tasks to the DPU and analyzing GPU telemetry and inter-node communication patterns, the resulting system can provide actionable feedback to inference controllers and schedulers. The goal of this study is three-fold i) identify the reported skews/imbalances/pathological conditions that arise in muti-GPU execution of a) LLM tensor computing (both during training and inference), b) identify their impact on computational performance, and c) make a critical assessment if those can be tracked for potential mitigation from a DPU network.

## 📝 요약

이 논문은 대규모 트랜스포머 기반 언어 모델(LLM)에서의 오토리그레시브 추론 시 발생하는 GPU 간 부하 불균형 문제를 해결하기 위해 DPU(데이터 처리 장치)를 활용한 프레임워크를 제안합니다. BlueField-3 DPU를 사용하여 실시간으로 부하 불균형을 감지하고 완화할 수 있으며, GPU 텔레메트리와 노드 간 통신 패턴을 분석하여 추론 컨트롤러와 스케줄러에 유용한 피드백을 제공합니다. 연구의 주요 목표는 다중 GPU 환경에서 발생하는 불균형 및 병리적 조건을 식별하고, 이들이 계산 성능에 미치는 영향을 평가하며, DPU 네트워크를 통해 이러한 문제를 추적하고 완화할 수 있는지를 비판적으로 평가하는 것입니다.

## 🎯 주요 포인트

- 1. 대규모 트랜스포머 기반 언어 모델에서 자회귀 추론 시 GPU 샤드 간 부하 불균형이 실행 효율성에 영향을 미친다.
- 2. BlueField-3 데이터 처리 장치를 활용한 DPU 지원 프레임워크는 멀티 노드 텐서 병렬 추론에서 부하 불균형을 실시간으로 감지하고 완화할 수 있다.
- 3. DPU에 모니터링 작업을 오프로드하고 GPU 원격 측정 및 노드 간 통신 패턴을 분석하여 추론 제어기와 스케줄러에 실행 가능한 피드백을 제공할 수 있다.
- 4. 연구의 목표는 다중 GPU 실행에서 발생하는 불균형 및 병리학적 조건을 식별하고, 이들이 계산 성능에 미치는 영향을 평가하며, DPU 네트워크를 통해 이를 추적하여 완화할 수 있는지 비판적으로 평가하는 것이다.


---

*Generated on 2025-09-24 14:45:01*
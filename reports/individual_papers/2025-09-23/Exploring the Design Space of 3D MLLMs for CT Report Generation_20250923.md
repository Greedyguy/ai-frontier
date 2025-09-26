---
keywords:
  - Multimodal Learning
  - Radiology Report Generation
  - Large Language Model
  - Segmentation Mask
  - Transformer
category: cs.LG
publish_date: 2025-09-23
arxiv_id: 2506.21535
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T03:05:52.557685",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Multimodal Learning",
    "Radiology Report Generation",
    "Large Language Model",
    "Segmentation Mask",
    "Transformer"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Multimodal Learning": 0.82,
    "Radiology Report Generation": 0.78,
    "Large Language Model": 0.85,
    "Segmentation Mask": 0.75,
    "Transformer": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Multimodal Large Language Models",
        "canonical": "Multimodal Learning",
        "aliases": [
          "MLLMs"
        ],
        "category": "specific_connectable",
        "rationale": "Multimodal Learning is crucial for integrating visual and textual data, enhancing connectivity with related multimodal research.",
        "novelty_score": 0.58,
        "connectivity_score": 0.87,
        "specificity_score": 0.78,
        "link_intent_score": 0.82
      },
      {
        "surface": "Radiology Report Generation",
        "canonical": "Radiology Report Generation",
        "aliases": [
          "RRG"
        ],
        "category": "unique_technical",
        "rationale": "This is a specific application area that connects to medical imaging and report automation research.",
        "novelty_score": 0.72,
        "connectivity_score": 0.65,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "Large Language Models",
        "canonical": "Large Language Model",
        "aliases": [
          "LLMs"
        ],
        "category": "broad_technical",
        "rationale": "LLMs are a foundational technology, linking to a wide range of NLP and AI research.",
        "novelty_score": 0.4,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.85
      },
      {
        "surface": "Segmentation Mask",
        "canonical": "Segmentation Mask",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "Segmentation masks are critical in medical imaging, linking to image processing and analysis techniques.",
        "novelty_score": 0.65,
        "connectivity_score": 0.7,
        "specificity_score": 0.8,
        "link_intent_score": 0.75
      },
      {
        "surface": "Vision Transformer",
        "canonical": "Transformer",
        "aliases": [
          "ViT"
        ],
        "category": "broad_technical",
        "rationale": "Vision Transformers are a key architecture in computer vision, connecting to transformer-based models.",
        "novelty_score": 0.5,
        "connectivity_score": 0.88,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "3D CT",
      "GREEN score",
      "AMOS-MM challenge"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Multimodal Large Language Models",
      "resolved_canonical": "Multimodal Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.58,
        "connectivity": 0.87,
        "specificity": 0.78,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "Radiology Report Generation",
      "resolved_canonical": "Radiology Report Generation",
      "decision": "linked",
      "scores": {
        "novelty": 0.72,
        "connectivity": 0.65,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Large Language Models",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Segmentation Mask",
      "resolved_canonical": "Segmentation Mask",
      "decision": "linked",
      "scores": {
        "novelty": 0.65,
        "connectivity": 0.7,
        "specificity": 0.8,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Vision Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.88,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Exploring the Design Space of 3D MLLMs for CT Report Generation

## 📋 메타데이터

**Links**: [[daily_digest_20250923|20250923]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2506.21535.pdf)
**Category**: cs.LG
**Published**: 2025-09-23
**ArXiv ID**: [2506.21535](https://arxiv.org/abs/2506.21535)

## 🔗 유사한 논문
- [[2025-09-19/Radiology Report Conditional 3D CT Generation with Multi Encoder Latent diffusion Model_20250919|Radiology Report Conditional 3D CT Generation with Multi Encoder Latent diffusion Model]] (85.7% similar)
- [[2025-09-22/Exploring the Capabilities of LLM Encoders for Image-Text Retrieval in Chest X-rays_20250922|Exploring the Capabilities of LLM Encoders for Image-Text Retrieval in Chest X-rays]] (84.3% similar)
- [[2025-09-23/Surgical-MambaLLM_ Mamba2-enhanced Multimodal Large Language Model for VQLA in Robotic Surgery_20250923|Surgical-MambaLLM: Mamba2-enhanced Multimodal Large Language Model for VQLA in Robotic Surgery]] (83.6% similar)
- [[2025-09-23/Medical AI Consensus_ A Multi-Agent Framework for Radiology Report Generation and Evaluation_20250923|Medical AI Consensus: A Multi-Agent Framework for Radiology Report Generation and Evaluation]] (83.5% similar)
- [[2025-09-23/SD-VLM_ Spatial Measuring and Understanding with Depth-Encoded Vision-Language Models_20250923|SD-VLM: Spatial Measuring and Understanding with Depth-Encoded Vision-Language Models]] (83.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]], [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Multimodal Learning|Multimodal Learning]]
**⚡ Unique Technical**: [[keywords/Radiology Report Generation|Radiology Report Generation]], [[keywords/Segmentation Mask|Segmentation Mask]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2506.21535v2 Announce Type: replace-cross 
Abstract: Multimodal Large Language Models (MLLMs) have emerged as a promising way to automate Radiology Report Generation (RRG). In this work, we systematically investigate the design space of 3D MLLMs, including visual input representation, projectors, Large Language Models (LLMs), and fine-tuning techniques for 3D CT report generation. We also introduce two knowledge-based report augmentation methods that improve performance on the GREEN score by up to 10%, achieving the 2nd place on the MICCAI 2024 AMOS-MM challenge. Our results on the 1,687 cases from the AMOS-MM dataset show that RRG is largely independent of the size of LLM under the same training protocol. We also show that larger volume size does not always improve performance if the original ViT was pre-trained on a smaller volume size. Lastly, we show that using a segmentation mask along with the CT volume improves performance. The code is publicly available at https://github.com/bowang-lab/AMOS-MM-Solution

## 📝 요약

이 연구는 방사선 보고서 생성 자동화를 위한 다중 모달 대형 언어 모델(MLLMs)의 설계 공간을 체계적으로 조사합니다. 3D CT 보고서 생성을 위해 시각적 입력 표현, 프로젝터, 대형 언어 모델(LLMs), 미세 조정 기법을 탐구하며, 두 가지 지식 기반 보고서 증강 방법을 도입하여 GREEN 점수를 최대 10% 향상시켰습니다. 연구 결과, 동일한 훈련 프로토콜 하에서 LLM의 크기와 RRG 성능은 크게 독립적이며, 원래 ViT가 작은 볼륨 크기로 사전 훈련된 경우 더 큰 볼륨 크기가 항상 성능을 향상시키지 않는다는 것을 보여줍니다. 또한, CT 볼륨과 함께 세분화 마스크를 사용하면 성능이 향상됨을 확인했습니다. 이 연구는 MICCAI 2024 AMOS-MM 챌린지에서 2위를 차지했으며, 관련 코드는 공개되어 있습니다.

## 🎯 주요 포인트

- 1. 3D 다중모달 대형 언어 모델(MLLMs)은 방사선 보고서 생성 자동화에 유망한 방법으로 부상하고 있다.
- 2. 3D CT 보고서 생성을 위한 시각적 입력 표현, 프로젝터, 대형 언어 모델(LLMs), 미세 조정 기술의 설계 공간을 체계적으로 조사하였다.
- 3. 두 가지 지식 기반 보고서 증강 방법을 도입하여 GREEN 점수를 최대 10% 향상시켰으며, MICCAI 2024 AMOS-MM 챌린지에서 2위를 차지했다.
- 4. 동일한 훈련 프로토콜 하에서 LLM의 크기가 RRG 성능에 크게 영향을 미치지 않는다는 것을 발견했다.
- 5. CT 볼륨과 함께 분할 마스크를 사용하면 성능이 향상된다는 것을 보여주었다.


---

*Generated on 2025-09-24 03:05:52*
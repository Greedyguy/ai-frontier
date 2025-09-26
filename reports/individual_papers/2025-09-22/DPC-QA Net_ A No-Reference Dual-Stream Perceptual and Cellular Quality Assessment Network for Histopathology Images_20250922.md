---
keywords:
  - DPC-QA Net
  - Attention Mechanism
  - Wavelet-based Perception
  - Whole Slide Imaging
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.15802
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:25:01.315254",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "DPC-QA Net",
    "Attention Mechanism",
    "Wavelet-based Perception",
    "Whole Slide Imaging"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "DPC-QA Net": 0.8,
    "Attention Mechanism": 0.78,
    "Wavelet-based Perception": 0.7,
    "Whole Slide Imaging": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "DPC-QA Net",
        "canonical": "DPC-QA Net",
        "aliases": [
          "Dual-Stream Perceptual and Cellular Quality Assessment Network"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel network architecture specific to the paper, crucial for linking to related works in histopathology image analysis.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Cross-attention fusion",
        "canonical": "Attention Mechanism",
        "aliases": [
          "Cross-attention"
        ],
        "category": "specific_connectable",
        "rationale": "Links to the broader concept of attention mechanisms, which are fundamental in neural network architectures.",
        "novelty_score": 0.4,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Wavelet-based global difference perception",
        "canonical": "Wavelet-based Perception",
        "aliases": [
          "Wavelet Perception"
        ],
        "category": "unique_technical",
        "rationale": "This technique is specific to the paper's approach and aids in connecting to image processing methods.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
      },
      {
        "surface": "Whole slide imaging",
        "canonical": "Whole Slide Imaging",
        "aliases": [
          "WSI"
        ],
        "category": "broad_technical",
        "rationale": "Essential for linking to the domain of digital pathology and image analysis.",
        "novelty_score": 0.3,
        "connectivity_score": 0.8,
        "specificity_score": 0.65,
        "link_intent_score": 0.75
      }
    ],
    "ban_list_suggestions": [
      "method",
      "performance",
      "experiment"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "DPC-QA Net",
      "resolved_canonical": "DPC-QA Net",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Cross-attention fusion",
      "resolved_canonical": "Attention Mechanism",
      "decision": "linked",
      "scores": {
        "novelty": 0.4,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Wavelet-based global difference perception",
      "resolved_canonical": "Wavelet-based Perception",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Whole slide imaging",
      "resolved_canonical": "Whole Slide Imaging",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.8,
        "specificity": 0.65,
        "link_intent": 0.75
      }
    }
  ]
}
-->

# DPC-QA Net: A No-Reference Dual-Stream Perceptual and Cellular Quality Assessment Network for Histopathology Images

**Korean Title:** DPC-QA Net: 조직병리학 이미지에 대한 무참조 이중 스트림 지각 및 세포 품질 평가 네트워크

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.15802.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.15802](https://arxiv.org/abs/2509.15802)

## 🔗 유사한 논문
- [[2025-09-22/DSDNet_ Raw Domain Demoir\'eing via Dual Color-Space Synergy_20250922|DSDNet: Raw Domain Demoir\'eing via Dual Color-Space Synergy]] (83.0% similar)
- [[2025-09-22/QWD-GAN_ Quality-aware Wavelet-driven GAN for Unsupervised Medical Microscopy Images Denoising_20250922|QWD-GAN: Quality-aware Wavelet-driven GAN for Unsupervised Medical Microscopy Images Denoising]] (81.8% similar)
- [[2025-09-22/USCTNet_ A deep unfolding nuclear-norm optimization solver for physically consistent HSI reconstruction_20250922|USCTNet: A deep unfolding nuclear-norm optimization solver for physically consistent HSI reconstruction]] (81.2% similar)
- [[2025-09-18/Generative AI for Misalignment-Resistant Virtual Staining to Accelerate Histopathology Workflows_20250918|Generative AI for Misalignment-Resistant Virtual Staining to Accelerate Histopathology Workflows]] (81.0% similar)
- [[2025-09-19/HPGN_ Hybrid Priors-Guided Network for Compressed Low-Light Image Enhancement_20250919|HPGN: Hybrid Priors-Guided Network for Compressed Low-Light Image Enhancement]] (80.4% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Whole Slide Imaging|Whole Slide Imaging]]
**🔗 Specific Connectable**: [[keywords/Attention Mechanism|Attention Mechanism]]
**⚡ Unique Technical**: [[keywords/DPC-QA Net|DPC-QA Net]], [[keywords/Wavelet-based Perception|Wavelet-based Perception]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15802v1 Announce Type: cross 
Abstract: Reliable whole slide imaging (WSI) hinges on image quality,yet staining artefacts, defocus, and cellular degradations are common. We present DPC-QA Net, a no-reference dual-stream network that couples wavelet-based global difference perception with cellular quality assessment from nuclear and membrane embeddings via an Aggr-RWKV module. Cross-attention fusion and multi-term losses align perceptual and cellular cues. Across different datasets, our model detects staining, membrane, and nuclear issues with >92% accuracy and aligns well with usability scores; on LIVEC and KonIQ it outperforms state-of-the-art NR-IQA. A downstream study further shows strong positive correlations between predicted quality and cell recognition accuracy (e.g., nuclei PQ/Dice, membrane boundary F-score), enabling practical pre-screening of WSI regions for computational pathology.

## 🔍 Abstract (한글 번역)

arXiv:2509.15802v1 발표 유형: 교차  
초록: 신뢰할 수 있는 전체 슬라이드 이미징(WSI)은 이미지 품질에 달려 있지만, 염색 인공물, 초점 흐림, 세포 열화가 흔히 발생합니다. 우리는 DPC-QA Net을 제안합니다. 이는 파형 기반의 전역 차이 인식을 세포 품질 평가와 결합하는 참조 없는 이중 스트림 네트워크로, Aggr-RWKV 모듈을 통해 핵 및 막 임베딩을 사용합니다. 교차 주의 융합과 다중 항 손실은 지각적 및 세포적 단서를 정렬합니다. 다양한 데이터셋에서, 우리의 모델은 염색, 막, 핵 문제를 92% 이상의 정확도로 감지하며, 사용성 점수와 잘 일치합니다. LIVEC와 KonIQ에서 최첨단 NR-IQA를 능가합니다. 후속 연구에서는 예측된 품질과 세포 인식 정확도(예: 핵 PQ/Dice, 막 경계 F-점수) 간의 강한 양의 상관관계를 보여주며, 계산 병리학을 위한 WSI 영역의 실용적인 사전 스크리닝을 가능하게 합니다.

## 📝 요약

이 논문은 이미지 품질이 중요한 전체 슬라이드 이미징(WSI)에서 발생할 수 있는 염색 아티팩트, 초점 흐림, 세포 열화를 해결하기 위해 DPC-QA Net이라는 무참조 이중 스트림 네트워크를 제안합니다. 이 모델은 웨이블릿 기반의 글로벌 차이 인식과 핵 및 세포막 임베딩을 통한 세포 품질 평가를 결합하며, Aggr-RWKV 모듈을 사용합니다. 교차 주의 융합과 다중 손실을 통해 인식적 및 세포적 신호를 정렬합니다. 다양한 데이터셋에서 이 모델은 염색, 세포막, 핵 문제를 92% 이상의 정확도로 감지하며, 사용성 점수와 잘 일치합니다. 또한, LIVEC 및 KonIQ 데이터셋에서 최신 NR-IQA를 능가합니다. 후속 연구에서는 예측된 품질과 세포 인식 정확도 간의 강한 양의 상관관계를 보여주며, 이는 계산 병리학을 위한 WSI 영역의 실용적인 사전 스크리닝을 가능하게 합니다.

## 🎯 주요 포인트

- 1. DPC-QA Net은 파형 기반의 글로벌 차이 인식과 세포 품질 평가를 결합한 무참조 이중 스트림 네트워크입니다.
- 2. Aggr-RWKV 모듈을 통해 핵과 막 임베딩에서 세포 품질을 평가합니다.
- 3. 크로스 어텐션 융합과 다중 항 손실을 통해 지각적 및 세포적 단서를 정렬합니다.
- 4. 다양한 데이터셋에서 염색, 막, 핵 문제를 92% 이상의 정확도로 감지하며, 사용성 점수와 잘 일치합니다.
- 5. 예측된 품질과 세포 인식 정확도 간의 강한 양의 상관관계를 보여, 계산 병리학을 위한 WSI 영역의 실질적인 사전 스크리닝을 가능하게 합니다.


---

*Generated on 2025-09-23 12:25:01*
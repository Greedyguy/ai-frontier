<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T16:25:30.864750",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Neural Network",
    "Frequency Low Cut Pooling",
    "Aliasing and Sinc Artifact-free Pooling",
    "Adversarial Attacks"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Neural Network": 0.85,
    "Frequency Low Cut Pooling": 0.7,
    "Aliasing and Sinc Artifact-free Pooling": 0.75,
    "Adversarial Attacks": 0.8
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Convolutional Neural Networks",
        "canonical": "Neural Network",
        "aliases": [
          "CNN",
          "Convolutional Networks"
        ],
        "category": "broad_technical",
        "rationale": "CNNs are a fundamental architecture in deep learning, relevant for linking with other neural network concepts.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Frequency Low Cut Pooling",
        "canonical": "Frequency Low Cut Pooling",
        "aliases": [
          "FLC Pooling"
        ],
        "category": "unique_technical",
        "rationale": "This is a novel downsampling method proposed in the paper, crucial for understanding its contributions.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.9,
        "link_intent_score": 0.7
      },
      {
        "surface": "Aliasing and Sinc Artifact-free Pooling",
        "canonical": "Aliasing and Sinc Artifact-free Pooling",
        "aliases": [
          "ASAP"
        ],
        "category": "unique_technical",
        "rationale": "ASAP is a key innovation in the paper, addressing aliasing issues in CNNs.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.92,
        "link_intent_score": 0.75
      },
      {
        "surface": "adversarial attacks",
        "canonical": "Adversarial Attacks",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "Adversarial attacks are a significant challenge in CNNs, relevant for linking with robustness studies.",
        "novelty_score": 0.5,
        "connectivity_score": 0.8,
        "specificity_score": 0.7,
        "link_intent_score": 0.8
      }
    ],
    "ban_list_suggestions": [
      "downsampling",
      "corruptions",
      "distribution shifts"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Convolutional Neural Networks",
      "resolved_canonical": "Neural Network",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Frequency Low Cut Pooling",
      "resolved_canonical": "Frequency Low Cut Pooling",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.9,
        "link_intent": 0.7
      }
    },
    {
      "candidate_surface": "Aliasing and Sinc Artifact-free Pooling",
      "resolved_canonical": "Aliasing and Sinc Artifact-free Pooling",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.92,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "adversarial attacks",
      "resolved_canonical": "Adversarial Attacks",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.8,
        "specificity": 0.7,
        "link_intent": 0.8
      }
    }
  ]
}
-->

# Fix your downsampling ASAP! Be natively more robust via Aliasing and Spectral Artifact free Pooling

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2307.09804.pdf)
**Category**: cs.CV
**Published**: 2025-09-24
**ArXiv ID**: [2307.09804](https://arxiv.org/abs/2307.09804)

## 🔗 유사한 논문
- [[2025-09-24/Reconstruction of Optical Coherence Tomography Images from Wavelength-space Using Deep-learning_20250924|Reconstruction of Optical Coherence Tomography Images from Wavelength-space Using Deep-learning]] (81.9% similar)
- [[2025-09-24/Moir\'eNet_ A Compact Dual-Domain Network for Image Demoir\'eing_20250924|Moir\'eNet: A Compact Dual-Domain Network for Image Demoir\'eing]] (81.5% similar)
- [[2025-09-22/DSDNet_ Raw Domain Demoir\'eing via Dual Color-Space Synergy_20250922|DSDNet: Raw Domain Demoir\'eing via Dual Color-Space Synergy]] (81.3% similar)
- [[2025-09-24/TriFusion-AE_ Language-Guided Depth and LiDAR Fusion for Robust Point Cloud Processing_20250924|TriFusion-AE: Language-Guided Depth and LiDAR Fusion for Robust Point Cloud Processing]] (81.2% similar)
- [[2025-09-23/R-Net_ A Reliable and Resource-Efficient CNN for Colorectal Cancer Detection with XAI Integration_20250923|R-Net: A Reliable and Resource-Efficient CNN for Colorectal Cancer Detection with XAI Integration]] (81.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Neural Network|Neural Network]]
**🔗 Specific Connectable**: [[keywords/Adversarial Attacks|Adversarial Attacks]]
**⚡ Unique Technical**: [[keywords/Frequency Low Cut Pooling|Frequency Low Cut Pooling]], [[keywords/Aliasing and Sinc Artifact-free Pooling|Aliasing and Sinc Artifact-free Pooling]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2307.09804v2 Announce Type: replace 
Abstract: Convolutional Neural Networks (CNNs) are successful in various computer vision tasks. From an image and signal processing point of view, this success is counter-intuitive, as the inherent spatial pyramid design of most CNNs is apparently violating basic signal processing laws, i.e. the Sampling Theorem in their downsampling operations. This issue has been broadly neglected until recent work in the context of adversarial attacks and distribution shifts showed that there is a strong correlation between the vulnerability of CNNs and aliasing artifacts induced by bandlimit-violating downsampling. As a remedy, we propose an alias-free downsampling operation in the frequency domain, denoted Frequency Low Cut Pooling (FLC Pooling) which we further extend to Aliasing and Sinc Artifact-free Pooling (ASAP). ASAP is alias-free and removes further artifacts from sinc-interpolation. Our experimental evaluation on ImageNet-1k, ImageNet-C and CIFAR datasets on various CNN architectures demonstrates that networks using FLC Pooling and ASAP as downsampling methods learn more stable features as measured by their robustness against common corruptions and adversarial attacks, while maintaining a clean accuracy similar to the respective baseline models.

## 📝 요약

이 논문은 CNN의 다운샘플링 과정에서 발생하는 에일리어싱 문제를 해결하기 위해 FLC Pooling과 ASAP이라는 새로운 방법을 제안합니다. 기존 CNN의 공간 피라미드 설계는 신호 처리의 기본 법칙을 위반하여 에일리어싱 아티팩트를 유발할 수 있습니다. 제안된 FLC Pooling과 ASAP는 주파수 영역에서 에일리어싱을 제거하고, 추가적인 아티팩트를 줄입니다. ImageNet-1k, ImageNet-C, CIFAR 데이터셋을 사용한 실험 결과, 이 방법들은 일반적인 왜곡과 적대적 공격에 대한 강인성을 높이면서도 기존 모델과 유사한 정확도를 유지하는 안정적인 특징을 학습함을 보여주었습니다.

## 🎯 주요 포인트

- 1. CNN의 다운샘플링 과정에서 발생하는 에일리어싱 문제는 최근 연구에서 취약성과 강한 상관관계가 있음이 밝혀졌다.
- 2. Frequency Low Cut Pooling (FLC Pooling)과 Aliasing and Sinc Artifact-free Pooling (ASAP)은 주파수 도메인에서 에일리어싱을 제거하는 다운샘플링 방법이다.
- 3. FLC Pooling과 ASAP을 사용한 네트워크는 일반적인 손상 및 적대적 공격에 대한 강인성이 향상되었다.
- 4. 제안된 방법은 기존 모델과 유사한 정확도를 유지하면서도 더 안정적인 특징을 학습한다.


---

*Generated on 2025-09-24 16:25:30*
<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T15:13:14.699729",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Deep Learning",
    "Optical Coherence Tomography",
    "Fourier Domain CNN",
    "Speckle Noise Reduction"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Deep Learning": 0.85,
    "Optical Coherence Tomography": 0.8,
    "Fourier Domain CNN": 0.78,
    "Speckle Noise Reduction": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Deep-Learning",
        "canonical": "Deep Learning",
        "aliases": [
          "DL"
        ],
        "category": "broad_technical",
        "rationale": "Deep Learning is a foundational technology in the proposed method, facilitating connections to a wide range of related research.",
        "novelty_score": 0.45,
        "connectivity_score": 0.9,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Optical Coherence Tomography",
        "canonical": "Optical Coherence Tomography",
        "aliases": [
          "OCT"
        ],
        "category": "unique_technical",
        "rationale": "OCT is the specific imaging technique being enhanced, making it a unique and central concept for linking.",
        "novelty_score": 0.75,
        "connectivity_score": 0.7,
        "specificity_score": 0.85,
        "link_intent_score": 0.8
      },
      {
        "surface": "Fourier Domain CNN",
        "canonical": "Fourier Domain CNN",
        "aliases": [
          "FD-CNN"
        ],
        "category": "unique_technical",
        "rationale": "FD-CNN is a novel application of CNNs in the Fourier domain, relevant for linking to advanced image processing techniques.",
        "novelty_score": 0.8,
        "connectivity_score": 0.65,
        "specificity_score": 0.8,
        "link_intent_score": 0.78
      },
      {
        "surface": "Speckle Noise Reduction",
        "canonical": "Speckle Noise Reduction",
        "aliases": [
          "Speckle Reduction"
        ],
        "category": "specific_connectable",
        "rationale": "Speckle noise reduction is a critical aspect of image quality improvement, linking to noise reduction techniques in imaging.",
        "novelty_score": 0.6,
        "connectivity_score": 0.75,
        "specificity_score": 0.7,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "Fourier-domain Optical Coherence Tomography",
      "encoder-decoder styled networks"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Deep-Learning",
      "resolved_canonical": "Deep Learning",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.9,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Optical Coherence Tomography",
      "resolved_canonical": "Optical Coherence Tomography",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.7,
        "specificity": 0.85,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Fourier Domain CNN",
      "resolved_canonical": "Fourier Domain CNN",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.65,
        "specificity": 0.8,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Speckle Noise Reduction",
      "resolved_canonical": "Speckle Noise Reduction",
      "decision": "linked",
      "scores": {
        "novelty": 0.6,
        "connectivity": 0.75,
        "specificity": 0.7,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Reconstruction of Optical Coherence Tomography Images from Wavelength-space Using Deep-learning

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.LG|cs.LG]]
**PDF**: [Download](https://arxiv.org/pdf/2509.18783.pdf)
**Category**: cs.LG
**Published**: 2025-09-24
**ArXiv ID**: [2509.18783](https://arxiv.org/abs/2509.18783)

## 🔗 유사한 논문
- [[2025-09-23/Single-Image Depth from Defocus with Coded Aperture and Diffusion Posterior Sampling_20250923|Single-Image Depth from Defocus with Coded Aperture and Diffusion Posterior Sampling]] (84.0% similar)
- [[2025-09-18/Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction for Sparse-View CT_20250918|Cross-Distribution Diffusion Priors-Driven Iterative Reconstruction for Sparse-View CT]] (83.1% similar)
- [[2025-09-24/A Kernel Space-based Multidimensional Sparse Model for Dynamic PET Image Denoising_20250924|A Kernel Space-based Multidimensional Sparse Model for Dynamic PET Image Denoising]] (83.1% similar)
- [[2025-09-24/A Single Image Is All You Need_ Zero-Shot Anomaly Localization Without Training Data_20250924|A Single Image Is All You Need: Zero-Shot Anomaly Localization Without Training Data]] (82.8% similar)
- [[2025-09-22/Recent Advancements in Microscopy Image Enhancement using Deep Learning_ A Survey_20250922|Recent Advancements in Microscopy Image Enhancement using Deep Learning: A Survey]] (82.5% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Deep Learning|Deep Learning]]
**🔗 Specific Connectable**: [[keywords/Speckle Noise Reduction|Speckle Noise Reduction]]
**⚡ Unique Technical**: [[keywords/Optical Coherence Tomography|Optical Coherence Tomography]], [[keywords/Fourier Domain CNN|Fourier Domain CNN]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.18783v1 Announce Type: cross 
Abstract: Conventional Fourier-domain Optical Coherence Tomography (FD-OCT) systems depend on resampling into wavenumber (k) domain to extract the depth profile. This either necessitates additional hardware resources or amplifies the existing computational complexity. Moreover, the OCT images also suffer from speckle noise, due to systemic reliance on low coherence interferometry. We propose a streamlined and computationally efficient approach based on Deep-Learning (DL) which enables reconstructing speckle-reduced OCT images directly from the wavelength domain. For reconstruction, two encoder-decoder styled networks namely Spatial Domain Convolution Neural Network (SD-CNN) and Fourier Domain CNN (FD-CNN) are used sequentially. The SD-CNN exploits the highly degraded images obtained by Fourier transforming the domain fringes to reconstruct the deteriorated morphological structures along with suppression of unwanted noise. The FD-CNN leverages this output to enhance the image quality further by optimization in Fourier domain (FD). We quantitatively and visually demonstrate the efficacy of the method in obtaining high-quality OCT images. Furthermore, we illustrate the computational complexity reduction by harnessing the power of DL models. We believe that this work lays the framework for further innovations in the realm of OCT image reconstruction.

## 📝 요약

이 논문은 기존의 푸리에 영역 광간섭단층촬영(FD-OCT) 시스템의 복잡성을 줄이고, 스페클 노이즈 문제를 해결하기 위해 딥러닝 기반의 새로운 방법론을 제안합니다. 제안된 방법은 파장 영역에서 직접 스페클이 감소된 OCT 이미지를 재구성하는 것으로, 두 개의 인코더-디코더 네트워크인 공간 도메인 CNN(SD-CNN)과 푸리에 도메인 CNN(FD-CNN)을 순차적으로 사용합니다. SD-CNN은 푸리에 변환을 통해 얻은 저해상도 이미지를 개선하고 노이즈를 억제하며, FD-CNN은 이를 바탕으로 푸리에 도메인에서 최적화하여 이미지 품질을 더욱 향상시킵니다. 이 방법은 높은 품질의 OCT 이미지를 얻는 데 효과적이며, 딥러닝 모델을 활용해 계산 복잡성을 줄이는 데 기여합니다. 이 연구는 OCT 이미지 재구성 분야의 혁신적 발전을 위한 기초를 마련합니다.

## 🎯 주요 포인트

- 1. 기존의 FD-OCT 시스템은 깊이 프로파일 추출을 위해 추가적인 하드웨어 자원이나 높은 계산 복잡성을 필요로 한다.
- 2. 제안된 방법은 딥러닝을 기반으로 하여 파장 도메인에서 직접 스펙클 노이즈가 감소된 OCT 이미지를 재구성한다.
- 3. SD-CNN과 FD-CNN 두 개의 인코더-디코더 네트워크를 순차적으로 사용하여 이미지 품질을 향상시킨다.
- 4. 제안된 방법은 OCT 이미지의 높은 품질을 정량적 및 시각적으로 입증하며, 계산 복잡성을 줄인다.
- 5. 본 연구는 OCT 이미지 재구성 분야에서의 추가적인 혁신을 위한 기초를 마련한다.


---

*Generated on 2025-09-24 15:13:14*
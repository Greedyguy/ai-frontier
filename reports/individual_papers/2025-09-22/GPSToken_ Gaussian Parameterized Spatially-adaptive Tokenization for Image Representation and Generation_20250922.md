---
keywords:
  - GPSToken
  - Transformer
  - Image Representation
  - Differentiable Renderer
category: cs.CV
publish_date: 2025-09-22
arxiv_id: 2509.01109
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-23T12:39:31.034669",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "GPSToken",
    "Transformer",
    "Image Representation",
    "Differentiable Renderer"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "GPSToken": 0.8,
    "Transformer": 0.75,
    "Image Representation": 0.78,
    "Differentiable Renderer": 0.7
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "GPSToken",
        "canonical": "GPSToken",
        "aliases": [
          "Gaussian Parameterized Spatially-adaptive Tokenization"
        ],
        "category": "unique_technical",
        "rationale": "GPSToken represents a novel framework for image tokenization, offering unique insights into adaptive image representation.",
        "novelty_score": 0.85,
        "connectivity_score": 0.65,
        "specificity_score": 0.9,
        "link_intent_score": 0.8
      },
      {
        "surface": "Transformer",
        "canonical": "Transformer",
        "aliases": [],
        "category": "broad_technical",
        "rationale": "Transformers are central to the proposed framework, facilitating the optimization of Gaussian parameters.",
        "novelty_score": 0.3,
        "connectivity_score": 0.9,
        "specificity_score": 0.6,
        "link_intent_score": 0.75
      },
      {
        "surface": "Image Representation",
        "canonical": "Image Representation",
        "aliases": [
          "Image Encoding"
        ],
        "category": "specific_connectable",
        "rationale": "Image representation is a core concept in the paper, linking it to broader computer vision tasks.",
        "novelty_score": 0.5,
        "connectivity_score": 0.85,
        "specificity_score": 0.7,
        "link_intent_score": 0.78
      },
      {
        "surface": "Differentiable Splatting-based Renderer",
        "canonical": "Differentiable Renderer",
        "aliases": [
          "Splatting Renderer"
        ],
        "category": "unique_technical",
        "rationale": "This renderer is crucial for reconstructing Gaussian parameterized tokens into feature maps, bridging tokenization with decoding.",
        "novelty_score": 0.75,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.7
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
      "candidate_surface": "GPSToken",
      "resolved_canonical": "GPSToken",
      "decision": "linked",
      "scores": {
        "novelty": 0.85,
        "connectivity": 0.65,
        "specificity": 0.9,
        "link_intent": 0.8
      }
    },
    {
      "candidate_surface": "Transformer",
      "resolved_canonical": "Transformer",
      "decision": "linked",
      "scores": {
        "novelty": 0.3,
        "connectivity": 0.9,
        "specificity": 0.6,
        "link_intent": 0.75
      }
    },
    {
      "candidate_surface": "Image Representation",
      "resolved_canonical": "Image Representation",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.85,
        "specificity": 0.7,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "Differentiable Splatting-based Renderer",
      "resolved_canonical": "Differentiable Renderer",
      "decision": "linked",
      "scores": {
        "novelty": 0.75,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.7
      }
    }
  ]
}
-->

# GPSToken: Gaussian Parameterized Spatially-adaptive Tokenization for Image Representation and Generation

**Korean Title:** GPSToken: 이미지 표현 및 생성을 위한 가우시안 매개 공간 적응형 토큰화

## 📋 메타데이터

**Links**: [[daily_digest_20250922|20250922]] [[categories/cs.CV|cs.CV]]
**PDF**: [Download](https://arxiv.org/pdf/2509.01109.pdf)
**Category**: cs.CV
**Published**: 2025-09-22
**ArXiv ID**: [2509.01109](https://arxiv.org/abs/2509.01109)

## 🔗 유사한 논문
- [[2025-09-19/AToken_ A Unified Tokenizer for Vision_20250919|AToken: A Unified Tokenizer for Vision]] (84.0% similar)
- [[2025-09-22/MaskAttn-SDXL_ Controllable Region-Level Text-To-Image Generation_20250922|MaskAttn-SDXL: Controllable Region-Level Text-To-Image Generation]] (81.4% similar)
- [[2025-09-18/Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images_20250918|Lightweight Gradient-Aware Upscaling of 3D Gaussian Splatting Images]] (81.1% similar)
- [[2025-09-22/Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance_20250922|Training-Free Pyramid Token Pruning for Efficient Large Vision-Language Models via Region, Token, and Instruction-Guided Importance]] (80.7% similar)
- [[2025-09-22/Layout Stroke Imitation_ A Layout Guided Handwriting Stroke Generation for Style Imitation with Diffusion Model_20250922|Layout Stroke Imitation: A Layout Guided Handwriting Stroke Generation for Style Imitation with Diffusion Model]] (80.6% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Transformer|Transformer]]
**🔗 Specific Connectable**: [[keywords/Image Representation|Image Representation]]
**⚡ Unique Technical**: [[keywords/GPSToken|GPSToken]], [[keywords/Differentiable Renderer|Differentiable Renderer]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.01109v2 Announce Type: replace 
Abstract: Effective and efficient tokenization plays an important role in image representation and generation. Conventional methods, constrained by uniform 2D/1D grid tokenization, are inflexible to represent regions with varying shapes and textures and at different locations, limiting their efficacy of feature representation. In this work, we propose $\textbf{GPSToken}$, a novel $\textbf{G}$aussian $\textbf{P}$arameterized $\textbf{S}$patially-adaptive $\textbf{Token}$ization framework, to achieve non-uniform image tokenization by leveraging parametric 2D Gaussians to dynamically model the shape, position, and textures of different image regions. We first employ an entropy-driven algorithm to partition the image into texture-homogeneous regions of variable sizes. Then, we parameterize each region as a 2D Gaussian (mean for position, covariance for shape) coupled with texture features. A specialized transformer is trained to optimize the Gaussian parameters, enabling continuous adaptation of position/shape and content-aware feature extraction. During decoding, Gaussian parameterized tokens are reconstructed into 2D feature maps through a differentiable splatting-based renderer, bridging our adaptive tokenization with standard decoders for end-to-end training. GPSToken disentangles spatial layout (Gaussian parameters) from texture features to enable efficient two-stage generation: structural layout synthesis using lightweight networks, followed by structure-conditioned texture generation. Experiments demonstrate the state-of-the-art performance of GPSToken, which achieves rFID and FID scores of 0.65 and 1.50 on image reconstruction and generation tasks using 128 tokens, respectively. Codes and models of GPSToken can be found at $\href{https://github.com/xtudbxk/GPSToken}{https://github.com/xtudbxk/GPSToken}$.

## 🔍 Abstract (한글 번역)

arXiv:2509.01109v2 발표 유형: 교체  
초록: 효과적이고 효율적인 토크나이제이션은 이미지 표현 및 생성에서 중요한 역할을 합니다. 기존 방법들은 균일한 2D/1D 그리드 토크나이제이션에 의해 제한되어, 다양한 모양과 질감을 가진 영역을 표현하는 데 유연하지 못하며, 위치가 다른 영역에서의 특징 표현의 효율성을 제한합니다. 본 연구에서는 $\textbf{GPSToken}$이라는 새로운 $\textbf{G}$aussian $\textbf{P}$arameterized $\textbf{S}$patially-adaptive $\textbf{Token}$ization 프레임워크를 제안하여, 파라메트릭 2D 가우시안을 활용하여 다양한 이미지 영역의 모양, 위치 및 질감을 동적으로 모델링함으로써 비균일 이미지 토크나이제이션을 달성합니다. 먼저, 엔트로피 기반 알고리즘을 사용하여 이미지를 다양한 크기의 질감 동질 영역으로 분할합니다. 그런 다음, 각 영역을 질감 특징과 결합된 2D 가우시안(위치를 위한 평균, 모양을 위한 공분산)으로 파라메터화합니다. 특수화된 트랜스포머가 가우시안 파라미터를 최적화하도록 훈련되어 위치/모양의 지속적인 적응과 콘텐츠 인식 특징 추출을 가능하게 합니다. 디코딩 시, 가우시안 파라미터화된 토큰은 차별 가능한 스플래팅 기반 렌더러를 통해 2D 특징 맵으로 재구성되어, 우리의 적응형 토크나이제이션과 표준 디코더를 연결하여 엔드 투 엔드 훈련을 가능하게 합니다. GPSToken은 공간 레이아웃(가우시안 파라미터)과 질감 특징을 분리하여 효율적인 2단계 생성을 가능하게 합니다: 경량 네트워크를 사용한 구조적 레이아웃 합성 후, 구조 조건부 질감 생성. 실험 결과, GPSToken은 이미지 재구성 및 생성 작업에서 각각 0.65와 1.50의 rFID 및 FID 점수를 기록하며 최첨단 성능을 입증합니다. GPSToken의 코드와 모델은 $\href{https://github.com/xtudbxk/GPSToken}{https://github.com/xtudbxk/GPSToken}$에서 찾을 수 있습니다.

## 📝 요약

이 논문에서는 이미지 표현 및 생성을 위한 효과적이고 효율적인 토큰화 방법인 GPSToken을 제안합니다. 기존의 균일한 2D/1D 그리드 토큰화의 한계를 극복하기 위해, GPSToken은 파라메트릭 2D 가우시안을 활용하여 이미지의 다양한 영역의 형태, 위치, 텍스처를 동적으로 모델링합니다. 먼저, 엔트로피 기반 알고리즘을 통해 텍스처가 균일한 영역으로 이미지를 분할하고, 각 영역을 2D 가우시안으로 파라메터화하여 위치와 형태를 나타냅니다. 특화된 트랜스포머를 통해 가우시안 파라미터를 최적화하여 위치와 형태의 연속적인 적응과 콘텐츠 인식 기능 추출을 가능하게 합니다. 실험 결과, GPSToken은 이미지 재구성과 생성 작업에서 뛰어난 성능을 보이며, rFID와 FID 점수에서 각각 0.65와 1.50을 기록했습니다.

## 🎯 주요 포인트

- 1. GPSToken은 2D 가우시안을 활용하여 이미지의 다양한 영역의 형태, 위치, 텍스처를 동적으로 모델링하여 비균일한 이미지 토큰화를 달성합니다.
- 2. 엔트로피 기반 알고리즘을 사용해 이미지를 텍스처가 균일한 가변 크기의 영역으로 분할하고, 각 영역을 2D 가우시안으로 매개변수화합니다.
- 3. 특화된 트랜스포머를 통해 가우시안 매개변수를 최적화하여 위치/형태의 연속적 적응과 콘텐츠 인식 기능 추출을 가능하게 합니다.
- 4. GPSToken은 구조적 레이아웃 합성과 구조 조건부 텍스처 생성을 통해 효율적인 2단계 생성을 지원합니다.
- 5. GPSToken은 이미지 재구성과 생성 작업에서 각각 0.65의 rFID와 1.50의 FID 점수를 기록하며 최첨단 성능을 입증했습니다.


---

*Generated on 2025-09-23 12:39:31*
<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-24T14:23:06.670760",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Large Language Model",
    "Vision-Language Model",
    "BLIPScore",
    "Caption-Image Alignment"
  ],
  "rejected_keywords": [],
  "similarity_scores": {
    "Large Language Model": 0.85,
    "Vision-Language Model": 0.82,
    "BLIPScore": 0.78,
    "Caption-Image Alignment": 0.77
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true,
  "candidates_json": {
    "candidates": [
      {
        "surface": "Large Language Model",
        "canonical": "Large Language Model",
        "aliases": [
          "LLM"
        ],
        "category": "broad_technical",
        "rationale": "Large Language Models are central to the paper's method for fusing captions, linking to broader NLP advancements.",
        "novelty_score": 0.45,
        "connectivity_score": 0.88,
        "specificity_score": 0.65,
        "link_intent_score": 0.85
      },
      {
        "surface": "Vision-Language",
        "canonical": "Vision-Language Model",
        "aliases": [
          "Vision-Language"
        ],
        "category": "evolved_concepts",
        "rationale": "The paper's focus on image captioning directly ties into the evolving field of Vision-Language Models.",
        "novelty_score": 0.55,
        "connectivity_score": 0.9,
        "specificity_score": 0.7,
        "link_intent_score": 0.82
      },
      {
        "surface": "BLIPScore",
        "canonical": "BLIPScore",
        "aliases": [],
        "category": "unique_technical",
        "rationale": "BLIPScore is a novel metric introduced in the paper, crucial for ranking image captions.",
        "novelty_score": 0.8,
        "connectivity_score": 0.6,
        "specificity_score": 0.85,
        "link_intent_score": 0.78
      },
      {
        "surface": "caption-image alignment",
        "canonical": "Caption-Image Alignment",
        "aliases": [],
        "category": "specific_connectable",
        "rationale": "This concept is key to evaluating the effectiveness of image captioning models.",
        "novelty_score": 0.5,
        "connectivity_score": 0.75,
        "specificity_score": 0.72,
        "link_intent_score": 0.77
      }
    ],
    "ban_list_suggestions": [
      "method",
      "experiment",
      "performance"
    ]
  },
  "decisions": [
    {
      "candidate_surface": "Large Language Model",
      "resolved_canonical": "Large Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.45,
        "connectivity": 0.88,
        "specificity": 0.65,
        "link_intent": 0.85
      }
    },
    {
      "candidate_surface": "Vision-Language",
      "resolved_canonical": "Vision-Language Model",
      "decision": "linked",
      "scores": {
        "novelty": 0.55,
        "connectivity": 0.9,
        "specificity": 0.7,
        "link_intent": 0.82
      }
    },
    {
      "candidate_surface": "BLIPScore",
      "resolved_canonical": "BLIPScore",
      "decision": "linked",
      "scores": {
        "novelty": 0.8,
        "connectivity": 0.6,
        "specificity": 0.85,
        "link_intent": 0.78
      }
    },
    {
      "candidate_surface": "caption-image alignment",
      "resolved_canonical": "Caption-Image Alignment",
      "decision": "linked",
      "scores": {
        "novelty": 0.5,
        "connectivity": 0.75,
        "specificity": 0.72,
        "link_intent": 0.77
      }
    }
  ]
}
-->

# Improving Image Captioning Descriptiveness by Ranking and LLM-based Fusion

## 📋 메타데이터

**Links**: [[daily_digest_20250924|20250924]] [[categories/cs.AI|cs.AI]]
**PDF**: [Download](https://arxiv.org/pdf/2306.11593.pdf)
**Category**: cs.AI
**Published**: 2025-09-24
**ArXiv ID**: [2306.11593](https://arxiv.org/abs/2306.11593)

## 🔗 유사한 논문
- [[2025-09-23/Pre-Trained CNN Architecture for Transformer-Based Image Caption Generation Model_20250923|Pre-Trained CNN Architecture for Transformer-Based Image Caption Generation Model]] (84.9% similar)
- [[2025-09-24/Align Where the Words Look_ Cross-Attention-Guided Patch Alignment with Contrastive and Transport Regularization for Bengali Captioning_20250924|Align Where the Words Look: Cross-Attention-Guided Patch Alignment with Contrastive and Transport Regularization for Bengali Captioning]] (83.8% similar)
- [[2025-09-18/Aligning Audio Captions with Human Preferences_20250918|Aligning Audio Captions with Human Preferences]] (83.6% similar)
- [[2025-09-23/Describe-to-Score_ Text-Guided Efficient Image Complexity Assessment_20250923|Describe-to-Score: Text-Guided Efficient Image Complexity Assessment]] (83.4% similar)
- [[2025-09-23/Captioning for Text-Video Retrieval via Dual-Group Direct Preference Optimization_20250923|Captioning for Text-Video Retrieval via Dual-Group Direct Preference Optimization]] (83.2% similar)

## 🏷️ 카테고리화된 키워드
**🧠 Broad Technical**: [[keywords/Large Language Model|Large Language Model]]
**🔗 Specific Connectable**: [[keywords/Caption-Image Alignment|Caption-Image Alignment]]
**⚡ Unique Technical**: [[keywords/BLIPScore|BLIPScore]]
**🚀 Evolved Concepts**: [[keywords/Vision-Language Model|Vision-Language Model]]

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2306.11593v2 Announce Type: replace-cross 
Abstract: State-of-The-Art (SoTA) image captioning models are often trained on the MicroSoft Common Objects in Context (MS-COCO) dataset, which contains human-annotated captions with an average length of approximately ten tokens. Although effective for general scene understanding, these short captions often fail to capture complex scenes and convey detailed information. Moreover, captioning models tend to exhibit bias towards the ``average'' caption, which captures only the more general aspects, thus overlooking finer details. In this paper, we present a novel approach to generate richer and more informative image captions by combining the captions generated from different SoTA captioning models. Our proposed method requires no additional model training: given an image, it leverages pre-trained models from the literature to generate the initial captions, and then ranks them using a newly introduced image-text-based metric, which we name BLIPScore. Subsequently, the top two captions are fused using a Large Language Model (LLM) to produce the final, more detailed description. Experimental results on the MS-COCO and Flickr30k test sets demonstrate the effectiveness of our approach in terms of caption-image alignment and hallucination reduction according to the ALOHa, CAPTURE, and Polos metrics. A subjective study lends additional support to these results, suggesting that the captions produced by our model are generally perceived as more consistent with human judgment. By combining the strengths of diverse SoTA models, our method enhances the quality and appeal of image captions, bridging the gap between automated systems and the rich and informative nature of human-generated descriptions. This advance enables the generation of more suitable captions for the training of both vision-language and captioning models.

## 📝 요약

이 논문은 이미지 캡셔닝 모델의 성능을 향상시키기 위한 새로운 접근법을 제안합니다. 기존의 MS-COCO 데이터셋을 활용한 모델들은 짧은 캡션을 생성하여 복잡한 장면의 세부사항을 놓치는 경향이 있습니다. 이를 해결하기 위해, 여러 최신 캡셔닝 모델에서 생성된 캡션을 결합하여 더 풍부하고 정보가 많은 캡션을 생성하는 방법을 소개합니다. 이 방법은 추가적인 모델 학습 없이, 사전 학습된 모델로부터 초기 캡션을 생성하고, 새롭게 제안된 BLIPScore라는 이미지-텍스트 기반 메트릭을 사용하여 이를 평가합니다. 상위 두 개의 캡션은 대형 언어 모델(LLM)을 통해 결합되어 최종 캡션을 만듭니다. 실험 결과, 이 방법은 MS-COCO와 Flickr30k 테스트 세트에서 캡션-이미지 정렬과 환각 감소 측면에서 우수한 성능을 보였습니다. 주관적 연구에서도 인간의 판단과 일치하는 캡션으로 평가되었습니다. 이 방법은 다양한 최신 모델의 강점을 결합하여 자동화된 시스템과 인간이 생성한 설명의 간극을 좁히는 데 기여합니다.

## 🎯 주요 포인트

- 1. 기존의 SoTA 이미지 캡셔닝 모델은 MS-COCO 데이터셋의 짧은 캡션에 의존하여 복잡한 장면을 충분히 설명하지 못하는 한계를 가집니다.
- 2. 본 연구는 다양한 SoTA 캡셔닝 모델에서 생성된 캡션을 결합하여 더 풍부하고 정보가 많은 이미지 캡션을 생성하는 새로운 방법을 제안합니다.
- 3. 제안된 방법은 추가적인 모델 훈련 없이 사전 훈련된 모델을 활용하며, BLIPScore라는 새로운 이미지-텍스트 기반 메트릭을 통해 캡션을 평가합니다.
- 4. 실험 결과, 제안된 방법은 MS-COCO 및 Flickr30k 테스트 세트에서 캡션-이미지 정렬과 환각 감소 측면에서 효과적임을 보여줍니다.
- 5. 주관적 연구 결과, 제안된 방법으로 생성된 캡션이 인간의 판단과 더 일치하는 것으로 평가되었습니다.


---

*Generated on 2025-09-24 14:23:06*
---
keywords:
  - Underwater Image Formation Model
  - Synthetic Data Generation
  - Forward Scattering
category: cs.AI
publish_date: 2025-09-18
arxiv_id:
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 22:11:17.662780",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Underwater Image Formation Model",
    "Synthetic Data Generation",
    "Forward Scattering"
  ],
  "rejected_keywords": [
    "Nonuniform Medium"
  ],
  "similarity_scores": {
    "Underwater Image Formation Model": 0.78,
    "Synthetic Data Generation": 0.72,
    "Forward Scattering": 0.75
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->

# Sea-ing Through Scattered Rays: Revisiting the Image Formation Model for Realistic Underwater Image Generation

**Korean Title:** 산란된 광선을 통한 바다 탐색: 현실적인 수중 이미지 생성을 위한 이미지 형성 모델 재검토

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250918|2025-09-18]]        [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🌐 Broad Technical**: [[keywords/Synthetic Data Generation|synthetic data generation]]
**⚡ Unique Technical**: [[keywords/Underwater Image Formation Model|underwater image formation model]], [[keywords/Forward Scattering|forward scattering]]

## 🔗 유사한 논문
- [[SPATIALGEN_ Layout-guided 3D Indoor Scene Generation_20250919|SPATIALGEN Layout-guided 3D Indoor Scene Generation]] (79.4% similar)
- [[Forecasting and Visualizing Air Quality from Sky Images with Vision-Language Models_20250919|Forecasting and Visualizing Air Quality from Sky Images with Vision-Language Models]] (79.0% similar)
- [[Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation_20250919|Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation]] (78.1% similar)
- [[TIDE_ Achieving Balanced Subject-Driven Image Generation via Target-Instructed Diffusion Enhancement_20250919|TIDE Achieving Balanced Subject-Driven Image Generation via Target-Instructed Diffusion Enhancement]] (78.1% similar)
- [[HPGN_ Hybrid Priors-Guided Network for Compressed Low-Light Image Enhancement_20250919|HPGN Hybrid Priors-Guided Network for Compressed Low-Light Image Enhancement]] (77.9% similar)

## 📋 저자 정보

**Authors:** Vasiliki Ismiroglou, Malte Pedersen, Stefan H. Bengtson, Andreas Aakerberg, Thomas B. Moeslund

## 📄 Abstract (원문)

In recent years, the underwater image formation model has found extensive use
in the generation of synthetic underwater data. Although many approaches focus
on scenes primarily affected by discoloration, they often overlook the model's
ability to capture the complex, distance-dependent visibility loss present in
highly turbid environments. In this work, we propose an improved synthetic data
generation pipeline that includes the commonly omitted forward scattering term,
while also considering a nonuniform medium. Additionally, we collected the
BUCKET dataset under controlled turbidity conditions to acquire real turbid
footage with the corresponding reference images. Our results demonstrate
qualitative improvements over the reference model, particularly under
increasing turbidity, with a selection rate of 82. 5\% by survey participants.
Data and code can be accessed on the project page:
vap.aau.dk/sea-ing-through-scattered-rays.

## 🔍 Abstract (한글 번역)

최근 몇 년 동안, 수중 이미지 형성 모델은 합성 수중 데이터 생성에 광범위하게 사용되고 있습니다. 많은 접근법이 주로 변색에 영향을 받는 장면에 집중하고 있지만, 이 모델이 고도로 탁한 환경에서 거리 의존적인 복잡한 가시성 손실을 포착하는 능력을 종종 간과합니다. 본 연구에서는 일반적으로 생략되는 전방 산란 항을 포함하면서 비균일 매질을 고려한 개선된 합성 데이터 생성 파이프라인을 제안합니다. 또한, 우리는 제어된 탁도 조건에서 BUCKET 데이터셋을 수집하여 해당 참조 이미지와 함께 실제 탁한 영상을 획득했습니다. 우리의 결과는 특히 탁도가 증가할수록 참조 모델에 비해 질적인 개선을 보여주며, 설문 조사 참가자들에 의해 82.5%의 선택률을 기록했습니다. 데이터와 코드는 프로젝트 페이지에서 확인할 수 있습니다: vap.aau.dk/sea-ing-through-scattered-rays.

## 📝 요약

이 연구는 수중 이미지 생성 모델을 개선하여 복잡한 탁도 환경에서 거리 의존적인 가시성 손실을 효과적으로 포착하는 방법을 제안합니다. 기존 모델들이 주로 색상 변화를 다루는 반면, 본 연구는 종종 생략되는 전방 산란 항을 포함하고 비균일 매체를 고려한 합성 데이터 생성 파이프라인을 개발했습니다. 또한, 통제된 탁도 조건에서 실제 탁도 영상을 수집한 BUCKET 데이터셋을 구축했습니다. 연구 결과, 기존 모델에 비해 탁도가 증가할수록 질적으로 개선된 결과를 보여주었으며, 설문 참여자 중 82.5%가 개선된 모델을 선택했습니다. 데이터와 코드는 프로젝트 페이지에서 확인할 수 있습니다.

## 🎯 주요 포인트

- 1. 본 연구는 기존의 수중 이미지 생성 모델에 흔히 생략되는 전방 산란 항을 포함하여 비균일 매체를 고려한 개선된 합성 데이터 생성 파이프라인을 제안합니다.

- 2. 통제된 탁도 조건 하에서 실제 탁한 영상과 해당 참조 이미지를 획득하기 위해 BUCKET 데이터셋을 수집했습니다.

- 3. 제안된 모델은 특히 탁도가 증가하는 상황에서 기존 참조 모델보다 질적으로 향상된 결과를 보여주었으며, 설문 조사 참가자들에 의해 82.5%의 선택률을 기록했습니다.

- 4. 연구 결과와 코드는 프로젝트 페이지(vap.aau.dk/sea-ing-through-scattered-rays)에서 접근할 수 있습니다.

---

*Generated on 2025-09-20 01:36:48*
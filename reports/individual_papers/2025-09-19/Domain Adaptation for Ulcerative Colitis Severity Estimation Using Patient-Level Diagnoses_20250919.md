---
keywords:
  - Transfer Learning
  - Weakly Supervised Learning
  - Ulcerative Colitis Severity Estimation
category: cs.AI
publish_date: 2025-09-19
arxiv_id: 2509.14573
---

<!-- KEYWORD_LINKING_METADATA:
{
  "processed_timestamp": "2025-09-22 21:47:30.910160",
  "vocabulary_version": "1.0",
  "selected_keywords": [
    "Transfer Learning",
    "Weakly Supervised Learning",
    "Ulcerative Colitis Severity Estimation"
  ],
  "rejected_keywords": [
    "Max-Severity Triplet Loss"
  ],
  "similarity_scores": {
    "Transfer Learning": 0.8,
    "Weakly Supervised Learning": 0.75,
    "Ulcerative Colitis Severity Estimation": 0.78
  },
  "extraction_method": "AI_prompt_based",
  "budget_applied": true
}
-->


# Domain Adaptation for Ulcerative Colitis Severity Estimation Using Patient-Level Diagnoses

**Korean Title:** 궤양성 대장염 중증도 추정을 위한 환자 수준 진단 기반 도메인 적응

## 📋 메타데이터

**Links**: [[digests/daily_digest_20250919|2025-09-19]]   [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔗 Specific Connectable**: [[keywords/Transfer Learning|Domain Adaptation]]
**⚡ Unique Technical**: [[keywords/Ulcerative Colitis Severity Estimation|Ulcerative Colitis Severity Estimation]]
**🚀 Evolved Concepts**: [[keywords/Weakly Supervised Learning|Weakly Supervised Domain Adaptation]]

## 🔗 유사한 논문
- [[BEVUDA++ Geometric-aware Unsupervised Domain Adaptation for Multi-View 3D Object Detection]] (79.8% similar)
- [[AD-DINOv3 Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration]] (77.8% similar)
- [[Fine-tuning Vision Language Models with Graph-based Knowledge for Explainable Medical Image Analysis_20250919|Fine-tuning Vision Language Models with Graph-based Knowledge for Explainable Medical Image Analysis]] (77.5% similar)
- [[Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation_20250919|Style Transfer with Diffusion Models for Synthetic-to-Real Domain Adaptation]] (77.5% similar)
- [[Ensemble of Pathology Foundation Models for MIDOG 2025 Track 2 Atypical Mitosis Classification]] (77.4% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.14573v1 Announce Type: new 
Abstract: The development of methods to estimate the severity of Ulcerative Colitis (UC) is of significant importance. However, these methods often suffer from domain shifts caused by differences in imaging devices and clinical settings across hospitals. Although several domain adaptation methods have been proposed to address domain shift, they still struggle with the lack of supervision in the target domain or the high cost of annotation. To overcome these challenges, we propose a novel Weakly Supervised Domain Adaptation method that leverages patient-level diagnostic results, which are routinely recorded in UC diagnosis, as weak supervision in the target domain. The proposed method aligns class-wise distributions across domains using Shared Aggregation Tokens and a Max-Severity Triplet Loss, which leverages the characteristic that patient-level diagnoses are determined by the most severe region within each patient. Experimental results demonstrate that our method outperforms comparative DA approaches, improving UC severity estimation in a domain-shifted setting.

## 🔍 Abstract (한글 번역)

arXiv:2509.14573v1 발표 유형: 신규  
초록: 궤양성 대장염(UC)의 중증도를 추정하는 방법의 개발은 매우 중요합니다. 그러나 이러한 방법들은 병원 간의 영상 장치 및 임상 환경의 차이로 인해 발생하는 도메인 변화로 인해 종종 어려움을 겪습니다. 도메인 변화를 해결하기 위해 여러 도메인 적응 방법이 제안되었지만, 여전히 대상 도메인에서의 감독 부족이나 높은 주석 비용 문제를 해결하지 못하고 있습니다. 이러한 문제를 극복하기 위해, 우리는 UC 진단에서 일상적으로 기록되는 환자 수준의 진단 결과를 대상 도메인에서 약한 감독으로 활용하는 새로운 약한 감독 도메인 적응 방법을 제안합니다. 제안된 방법은 공유 집계 토큰과 환자 수준의 진단이 각 환자 내에서 가장 심각한 부위에 의해 결정된다는 특성을 활용하는 최대 중증도 삼중 손실을 사용하여 도메인 간의 클래스별 분포를 정렬합니다. 실험 결과는 제안된 방법이 비교 도메인 적응 접근법보다 우수하며, 도메인 변화된 환경에서 UC 중증도 추정을 개선함을 보여줍니다.

## 📝 요약

이 논문은 궤양성 대장염(UC) 심각도를 추정하는 방법 개발의 중요성을 다루고 있습니다. 기존 방법들은 병원 간의 영상 장비 및 임상 환경 차이로 인한 도메인 이동 문제를 겪고 있습니다. 이를 해결하기 위해 제안된 여러 도메인 적응 방법들은 목표 도메인에서의 감독 부족이나 높은 주석 비용 문제를 여전히 가지고 있습니다. 본 연구에서는 환자 수준의 진단 결과를 약한 감독으로 활용하는 새로운 약한 감독 도메인 적응 방법을 제안합니다. 이 방법은 공유 집계 토큰과 최대 심각도 삼중 손실을 사용하여 도메인 간 클래스별 분포를 정렬합니다. 실험 결과, 제안된 방법이 도메인 이동 환경에서 UC 심각도 추정 성능을 향상시키며 기존 방법들보다 우수함을 보여줍니다.

## 🎯 주요 포인트

- 1. 궤양성 대장염(UC) 중증도를 추정하는 방법 개발은 매우 중요하지만, 병원 간 영상 장치 및 임상 환경의 차이로 인한 도메인 이동 문제를 겪고 있습니다.

- 2. 기존 도메인 적응 방법들은 목표 도메인에서의 감독 부족이나 높은 주석 비용 문제를 해결하지 못하고 있습니다.

- 3. 우리는 환자 수준의 진단 결과를 약한 감독으로 활용하는 새로운 약한 감독 도메인 적응 방법을 제안합니다.

- 4. 제안된 방법은 공유 집계 토큰과 Max-Severity Triplet Loss를 사용하여 도메인 간 클래스별 분포를 정렬합니다.

- 5. 실험 결과, 제안된 방법이 도메인 이동 환경에서 UC 중증도 추정 성능을 개선하며 비교 도메인 적응 접근법보다 우수함을 보여줍니다.

---

*Generated on 2025-09-19 16:04:35*
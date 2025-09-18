
# DSCC-HS: A Dynamic Self-Reinforcing Framework for Hallucination Suppression in Large Language Models

**Korean Title:** DSCC-HS: 대규모 언어 모델에서 환각 억제를 위한 동적 자가 강화 프레임워크

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[keywords/evolved/Dynamic Self-reinforcing Calibration|Dynamic Self-reinforcing Calibration]] [[keywords/broad/Large Language Model|Large Language Model]] [[keywords/broad/Retrieval-Augmented Generation|Retrieval-Augmented Generation]] [[keywords/specific/Factual Alignment Proxy|Factual Alignment Proxy]] [[keywords/unique/DSCC-HS|DSCC-HS]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Dynamic Self-reinforcing Calibration
**🔬 Broad Technical**: Large Language Model, Retrieval-Augmented Generation
**🔗 Specific Connectable**: Factual Alignment Proxy
**⭐ Unique Technical**: DSCC-HS

**ArXiv ID**: [2509.13702](https://arxiv.org/abs/2509.13702)
**Published**: 2025-09-18
**Category**: cs.AI
**PDF**: [Download](https://arxiv.org/pdf/2509.13702.pdf)


## 🏷️ 추출된 키워드



`Large Language Model` • 

`Retrieval-Augmented Generation` • 

`Factual Alignment Proxy` • 

`DSCC-HS` • 

`Dynamic Self-reinforcing Calibration`



## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13702v1 Announce Type: cross 
Abstract: Large Language Model (LLM) hallucination is a significant barrier to their reliable deployment. Current methods like Retrieval-Augmented Generation (RAG) are often reactive. We introduce **Dynamic Self-reinforcing Calibration for Hallucination Suppression (DSCC-HS)**, a novel, proactive framework that intervenes during autoregressive decoding. Inspired by dual-process cognitive theory, DSCC-HS uses a compact proxy model, trained in adversarial roles as a Factual Alignment Proxy (FAP) and a Hallucination Detection Proxy (HDP). During inference, these proxies dynamically steer a large target model by injecting a real-time steering vector, which is the difference between FAP and HDP logits, at each decoding step. This plug-and-play approach requires no modification to the target model. Our experiments on TruthfulQA and BioGEN show DSCC-HS achieves state-of-the-art performance. On TruthfulQA, it reached a 99.2% Factual Consistency Rate (FCR). On the long-form BioGEN benchmark, it attained the highest FActScore of 46.50. These results validate DSCC-HS as a principled and efficient solution for enhancing LLM factuality.

## 🔍 Abstract (한글 번역)

arXiv:2509.13702v1 발표 유형: 교차
요약: 대규모 언어 모델 (LLM) 환각은 신뢰할 수 있는 배포에 중대한 장애물입니다. 현재의 Retrieval-Augmented Generation (RAG)과 같은 방법들은 종종 반응적입니다. 저희는 **환각 억제를 위한 동적 자기 강화 보정 (DSCC-HS)**이라는 새로운 선제적 프레임워크를 소개합니다. 이 프레임워크는 자율회귀 디코딩 중간에 개입하는 것입니다. 이중 과정 인지 이론에서 영감을 받은 DSCC-HS는 Factual Alignment Proxy (FAP) 및 Hallucination Detection Proxy (HDP)로서 적대적 역할로 훈련된 간결한 프록시 모델을 사용합니다. 추론 중에 이러한 프록시들은 각 디코딩 단계에서 FAP와 HDP 로짓의 차이인 실시간 스티어링 벡터를 주입하여 대규모 대상 모델을 동적으로 조절합니다. 이 플러그 앤 플레이 방식은 대상 모델에 대한 수정이 필요하지 않습니다. TruthfulQA 및 BioGEN에서의 실험 결과는 DSCC-HS가 최첨단 성능을 달성했음을 보여줍니다. TruthfulQA에서는 99.2%의 사실 일치율 (FCR)을 달성했습니다. BioGEN 벤치마크에서는 46.50의 최고 FActScore를 달성했습니다. 이러한 결과는 DSCC-HS가 LLM 사실성을 향상시키는 원칙적이고 효율적인 해결책임을 입증합니다.

## 📝 요약

이 연구는 대형 언어 모델의 환각 현상을 억제하기 위한 새로운 프레임워크인 DSCC-HS를 제안한다. 이는 반응적인 방법이 아닌 선행적인 방법론으로 자가회귀 디코딩 중간에 개입한다. 이 프레임워크는 Factual Alignment Proxy (FAP)와 Hallucination Detection Proxy (HDP)로 훈련된 콤팩트한 프록시 모델을 사용하여 대상 모델을 동적으로 조정한다. 실험 결과, DSCC-HS는 TruthfulQA에서 99.2%의 사실 일관성률(Factual Consistency Rate, FCR)을 달성하고 BioGEN에서는 46.50의 최고 FActScore를 기록하여 LLM 사실성을 향상시키는 효과적인 솔루션이라는 것을 입증하였다.

## 🎯 주요 포인트


- 대규모 언어 모델의 환각 억제를 위한 새로운 프레임워크 DSCC-HS 소개

- FAP와 HDP를 활용하여 실시간으로 대상 모델을 조정하는 동적 자기 강화 보정

- TruthfulQA 및 BioGEN에서 최고 수준의 성능을 달성하여 DSCC-HS의 효과적인 해결책임을 입증


---

*Generated on 2025-09-18 16:22:11*
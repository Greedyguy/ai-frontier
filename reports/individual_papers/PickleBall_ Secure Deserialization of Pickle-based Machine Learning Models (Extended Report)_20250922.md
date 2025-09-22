# PickleBall: Secure Deserialization of Pickle-based Machine Learning Models (Extended Report)

**Korean Title:** 피클볼: 피클 기반 머신러닝 모델의 안전한 역직렬화 (확장 보고서)

## 📋 메타데이터

## 📋 메타데이터

**Links**: [[reports/digests/daily_digest_20250922|2025-09-22]] [[keywords/evolved/Safe Model Loading|Safe Model Loading]] [[keywords/specific/Static Code Analysis|Static Code Analysis]] [[keywords/broad/Machine Learning Security|Machine Learning Security]] [[keywords/unique/PickleBall|PickleBall]] [[categories/cs.LG|cs.LG]] [[2025-09-22/Activation Space Interventions Can Be Transferred Between Large Language Models_20250922|Activation Space Interventions Can Be Transferred Between Large Language Models]] (82.0% similar) [[2025-09-19/Manipulation Facing Threats_ Evaluating Physical Vulnerabilities in End-to-End Vision Language Action Models_20250919|Manipulation Facing Threats: Evaluating Physical Vulnerabilities in End-to-End Vision Language Action Models]] (79.3% similar) [[2025-09-19/Enterprise AI Must Enforce Participant-Aware Access Control_20250919|Enterprise AI Must Enforce Participant-Aware Access Control]] (79.2% similar)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Safe Model Loading
**🔗 Specific Connectable**: Static Code Analysis
**🔬 Broad Technical**: Machine Learning Security
**⭐ Unique Technical**: PickleBall
## 🔗 유사한 논문
- [[2025-09-22/Activation Space Interventions Can Be Transferred Between Large Language Models_20250922|Activation Space Interventions Can Be Transferred Between Large Language Models]] (82.0% similar)
- [[2025-09-19/Manipulation Facing Threats_ Evaluating Physical Vulnerabilities in End-to-End Vision Language Action Models_20250919|Manipulation Facing Threats Evaluating Physical Vulnerabilities in End-to-End Vision Language Action Models]] (79.3% similar)
- [[2025-09-19/Enterprise AI Must Enforce Participant-Aware Access Control_20250919|Enterprise AI Must Enforce Participant-Aware Access Control]] (79.2% similar)
- [[2025-09-19/BEACON_ Behavioral Malware Classification with Large Language Model Embeddings and Deep Learning_20250919|BEACON Behavioral Malware Classification with Large Language Model Embeddings and Deep Learning]] (78.7% similar)
- [[2025-09-19/Adversarial Distilled Retrieval-Augmented Guarding Model for Online Malicious Intent Detection_20250919|Adversarial Distilled Retrieval-Augmented Guarding Model for Online Malicious Intent Detection]] (78.7% similar)


**ArXiv ID**: [2508.15987](https://arxiv.org/abs/2508.15987)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2508.15987.pdf)


**ArXiv ID**: [2508.15987](https://arxiv.org/abs/2508.15987)
**Published**: 2025-09-22
**Category**: cs.LG
**PDF**: [Download](https://arxiv.org/pdf/2508.15987.pdf)

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Secure Model Loading
**🔗 Specific Connectable**: Static Code Analysis
**⭐ Unique Technical**: PickleBall
**🔬 Broad Technical**: Machine Learning Security

## 🏷️ 추출된 키워드



`Machine Learning Security` • 

`Static Analysis` • 

`PickleBall` • 

`Safe Model Loading`



## 🔗 유사한 논문

Similar papers will be displayed here based on embedding similarity.

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2508.15987v2 Announce Type: replace-cross 
Abstract: Machine learning model repositories such as the Hugging Face Model Hub facilitate model exchanges. However, bad actors can deliver malware through compromised models. Existing defenses such as safer model formats, restrictive (but inflexible) loading policies, and model scanners have shortcomings: 44.9% of popular models on Hugging Face still use the insecure pickle format, 15% of these cannot be loaded by restrictive loading policies, and model scanners have both false positives and false negatives. Pickle remains the de facto standard for model exchange, and the ML community lacks a tool that offers transparent safe loading.
  We present PickleBall to help machine learning engineers load pickle-based models safely. PickleBall statically analyzes the source code of a given machine learning library and computes a custom policy that specifies a safe load-time behavior for benign models. PickleBall then dynamically enforces the policy during load time as a drop-in replacement for the pickle module. PickleBall generates policies that correctly load 79.8% of benign pickle-based models in our dataset, while rejecting all (100%) malicious examples in our dataset. In comparison, evaluated model scanners fail to identify known malicious models, and the state-of-art loader loads 22% fewer benign models than PickleBall. PickleBall removes the threat of arbitrary function invocation from malicious pickle-based models, raising the bar for attackers to depend on code reuse techniques.

## 🔍 Abstract (한글 번역)

arXiv:2508.15987v2 발표 유형: 교차 교체  
초록: Hugging Face Model Hub과 같은 기계 학습 모델 저장소는 모델 교환을 용이하게 합니다. 그러나 악의적인 행위자는 손상된 모델을 통해 악성 소프트웨어를 전달할 수 있습니다. 더 안전한 모델 형식, 제한적(그러나 유연하지 않은) 로딩 정책, 모델 스캐너와 같은 기존 방어 수단에는 단점이 있습니다: Hugging Face의 인기 있는 모델 중 44.9%는 여전히 안전하지 않은 pickle 형식을 사용하고 있으며, 이 중 15%는 제한적인 로딩 정책으로 로드할 수 없으며, 모델 스캐너는 오탐지와 미탐지를 모두 가지고 있습니다. Pickle은 여전히 모델 교환의 사실상 표준이며, ML 커뮤니티는 투명하고 안전한 로딩을 제공하는 도구가 부족합니다.  
우리는 기계 학습 엔지니어들이 pickle 기반 모델을 안전하게 로드할 수 있도록 돕기 위해 PickleBall을 제안합니다. PickleBall은 주어진 기계 학습 라이브러리의 소스 코드를 정적으로 분석하고, 안전한 로드 시간 동작을 명시하는 사용자 정의 정책을 계산합니다. 그런 다음 PickleBall은 pickle 모듈의 대체물로서 로드 시간 동안 정책을 동적으로 적용합니다. PickleBall은 데이터셋에서 79.8%의 정상적인 pickle 기반 모델을 올바르게 로드하는 정책을 생성하며, 데이터셋의 모든(100%) 악성 예제를 거부합니다. 비교해보면, 평가된 모델 스캐너는 알려진 악성 모델을 식별하지 못하며, 최신 로더는 PickleBall보다 22% 적은 정상 모델을 로드합니다. PickleBall은 악성 pickle 기반 모델에서 임의의 함수 호출 위협을 제거하여 공격자가 코드 재사용 기술에 의존해야 하는 장벽을 높입니다.

## 📝 요약

이 논문은 머신러닝 모델 저장소에서 악성 소프트웨어 전파를 방지하기 위한 도구인 PickleBall을 제안합니다. 기존의 안전한 모델 형식, 제한적인 로딩 정책, 모델 스캐너는 각각의 한계가 있습니다. PickleBall은 머신러닝 라이브러리의 소스 코드를 정적으로 분석하여 안전한 로딩 정책을 생성하고, 로딩 시 동적으로 이를 적용합니다. 실험 결과, PickleBall은 79.8%의 정상적인 pickle 기반 모델을 안전하게 로드하고, 모든 악성 모델을 차단했습니다. 이는 기존 스캐너와 로더보다 우수한 성능을 보여줍니다.

## 🎯 주요 포인트


- 1. 많은 인기 있는 머신러닝 모델이 여전히 보안에 취약한 pickle 형식을 사용하고 있습니다.

- 2. 기존의 보안 대책들은 제한적이거나 유연성이 부족하여 효과적이지 않습니다.

- 3. PickleBall은 안전한 모델 로딩을 위해 사용자 정의 정책을 생성하고 이를 실행 시 동적으로 적용합니다.

- 4. PickleBall은 데이터셋 내 악성 모델을 100% 차단하면서도 79.8%의 정상 모델을 올바르게 로드합니다.

- 5. PickleBall은 악성 pickle 기반 모델의 임의 함수 호출 위협을 제거하여 공격자들의 코드 재사용 기술 의존도를 높입니다.


---

*Generated on 2025-09-22 16:15:06*

# SNaRe: Domain-aware Data Generation for Low-Resource Event Detection

**Korean Title:** SNaRe: 저자원 이벤트 탐지를 위한 도메인 인식 데이터 생성

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Domain-aware Data Generation

## 🔗 유사한 논문
- [[DeKeyNLU Enhancing Natural Language to SQL Generation through Task Decomposition and Keyword Extraction]] (78.1% similar)
- [[Evolution Meets Diffusion Efficient Neural Architecture Generation]] (77.9% similar)
- [[Enhancing_Retrieval_Augmentation_via_Adversarial_Collaboration_20250919|Enhancing Retrieval Augmentation via Adversarial Collaboration]] (77.2% similar)
- [[AD-DINOv3 Enhancing DINOv3 for Zero-Shot Anomaly Detection with Anomaly-Aware Calibration]] (77.1% similar)
- [[BERTector An Intrusion Detection Framework Constructed via Joint-dataset Learning Based on Language Model]] (76.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.17394v3 Announce Type: replace-cross 
Abstract: Event Detection (ED) -- the task of identifying event mentions from natural language text -- is critical for enabling reasoning in highly specialized domains such as biomedicine, law, and epidemiology. Data generation has proven to be effective in broadening its utility to wider applications without requiring expensive expert annotations. However, when existing generation approaches are applied to specialized domains, they struggle with label noise, where annotations are incorrect, and domain drift, characterized by a distributional mismatch between generated sentences and the target domain. To address these issues, we introduce SNaRe, a domain-aware synthetic data generation framework composed of three components: Scout, Narrator, and Refiner. Scout extracts triggers from unlabeled target domain data and curates a high-quality domain-specific trigger list using corpus-level statistics to mitigate domain drift. Narrator, conditioned on these triggers, generates high-quality domain-aligned sentences, and Refiner identifies additional event mentions, ensuring high annotation quality. Experimentation on three diverse domain ED datasets reveals how SNaRe outperforms the best baseline, achieving average F1 gains of 3-7% in the zero-shot/few-shot settings and 4-20% F1 improvement for multilingual generation. Analyzing the generated trigger hit rate and human evaluation substantiates SNaRe's stronger annotation quality and reduced domain drift.

## 🔍 Abstract (한글 번역)

arXiv:2502.17394v3 발표 유형: 교체-교차  
초록: 이벤트 감지(ED) - 자연어 텍스트에서 이벤트 언급을 식별하는 작업 - 는 생물의학, 법률, 역학과 같은 고도로 전문화된 분야에서 추론을 가능하게 하는 데 중요합니다. 데이터 생성은 비싼 전문가 주석 없이도 더 넓은 응용 분야로 그 유용성을 확장하는 데 효과적임이 입증되었습니다. 그러나 기존의 생성 접근 방식을 전문화된 분야에 적용할 때, 주석이 잘못된 레이블 노이즈와 생성된 문장과 목표 도메인 간의 분포 불일치로 특징지어지는 도메인 드리프트에 어려움을 겪습니다. 이러한 문제를 해결하기 위해 우리는 Scout, Narrator, Refiner라는 세 가지 구성 요소로 구성된 도메인 인식 합성 데이터 생성 프레임워크인 SNaRe를 소개합니다. Scout는 레이블이 없는 목표 도메인 데이터에서 트리거를 추출하고 코퍼스 수준의 통계를 사용하여 도메인 드리프트를 완화하는 고품질 도메인별 트리거 목록을 큐레이팅합니다. Narrator는 이러한 트리거를 조건으로 하여 고품질 도메인 정렬 문장을 생성하고, Refiner는 추가 이벤트 언급을 식별하여 높은 주석 품질을 보장합니다. 세 가지 다양한 도메인 ED 데이터셋에 대한 실험은 SNaRe가 가장 뛰어난 기준선을 능가하여 제로샷/소수샷 설정에서 평균 F1 3-7% 향상과 다국어 생성에서 4-20% F1 향상을 달성하는 방법을 보여줍니다. 생성된 트리거 적중률과 인간 평가 분석은 SNaRe의 강력한 주석 품질과 감소된 도메인 드리프트를 입증합니다.

## 📝 요약

이 논문은 자연어 텍스트에서 이벤트를 식별하는 작업인 이벤트 감지(ED)의 중요성을 강조하며, 특히 생물의학, 법률, 역학 등 전문 분야에서의 활용을 다룹니다. 기존 데이터 생성 방법이 전문 분야에 적용될 때 라벨 오류와 도메인 드리프트 문제를 겪는다는 점을 지적하며, 이를 해결하기 위해 SNaRe라는 도메인 인식 합성 데이터 생성 프레임워크를 제안합니다. SNaRe는 Scout, Narrator, Refiner의 세 가지 구성 요소로 이루어져 있으며, 각각 트리거 추출, 도메인 정렬 문장 생성, 추가 이벤트 식별을 담당합니다. 실험 결과, SNaRe는 다양한 도메인 ED 데이터셋에서 기존 방법보다 평균 F1 점수를 3-7% 향상시켰으며, 다국어 생성에서도 4-20%의 F1 개선을 보였습니다. 트리거 적중률 및 인간 평가 분석을 통해 SNaRe의 높은 주석 품질과 감소된 도메인 드리프트가 입증되었습니다.

## 🎯 주요 포인트

- 1. Event Detection(ED)은 자연어 텍스트에서 이벤트 언급을 식별하는 작업으로, 생의학, 법률, 역학과 같은 전문 분야에서 중요한 역할을 한다.

- 2. 기존 데이터 생성 접근 방식은 레이블 노이즈와 도메인 드리프트 문제를 겪으며, 이를 해결하기 위해 SNaRe라는 도메인 인식 합성 데이터 생성 프레임워크가 제안되었다.

- 3. SNaRe는 Scout, Narrator, Refiner의 세 가지 구성 요소로 이루어져 있으며, 각각 도메인 특화 트리거 목록 생성, 도메인 정렬 문장 생성, 추가 이벤트 언급 식별을 담당한다.

- 4. SNaRe는 다양한 도메인 ED 데이터셋 실험에서 최고 기준을 능가하며, 제로샷/소수샷 설정에서 평균 F1 점수 3-7% 향상, 다국어 생성에서 4-20% F1 개선을 달성했다.

- 5. 생성된 트리거 적중률 및 인간 평가 분석은 SNaRe의 높은 주석 품질과 감소된 도메인 드리프트를 입증한다.

---

*Generated on 2025-09-19 15:11:29*
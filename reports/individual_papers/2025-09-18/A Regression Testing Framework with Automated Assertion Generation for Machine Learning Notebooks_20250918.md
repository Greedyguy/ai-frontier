
# A Regression Testing Framework with Automated Assertion Generation for Machine Learning Notebooks

**Korean Title:** 기계 학습 노트북을 위한 자동 어설션 생성을 갖춘 회귀 테스트 프레임워크

## 📋 메타데이터

**Links**: [[daily/2025-09-18|2025-09-18]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Mutation Score

## 🔗 유사한 논문
- [[An Empirical Study on Failures in Automated Issue Solving]] (74.0% similar)
- [[Accelerated Gradient Methods with Biased Gradient Estimates: Risk Sensitivity, High-Probability Guarantees, and Large Deviation Bounds]] (73.4% similar)
- [[PhysicalAgent: Towards General Cognitive Robotics with Foundation World Models]] (73.2% similar)
- [[BERTector_An_Intrusion_Detection_Framework_Constructed_via_Joint-dataset_Learning_Based_on_Language_Model_20250918|BERTector: An Intrusion Detection Framework Constructed via Joint-dataset Learning Based on Language Model]] (72.8% similar)
- [[DiffGAN_A_Test_Generation_Approach_for_Differential_Testing_of_Deep_Neural_Networks_for_Image_Analysis_20250918|DiffGAN: A Test Generation Approach for Differential Testing of Deep Neural Networks for Image Analysis]] (72.7% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.13656v1 Announce Type: new 
Abstract: Notebooks have become the de-facto choice for data scientists and machine learning engineers for prototyping and experimenting with machine learning (ML) pipelines. Notebooks provide an interactive interface for code, data, and visualization. However, notebooks provide very limited support for testing. Thus, during continuous development, many subtle bugs that do not lead to crashes often go unnoticed and cause silent errors that manifest as performance regressions.
  To address this, we introduce NBTest - the first regression testing framework that allows developers to write cell-level assertions in notebooks and run such notebooks in pytest or in continuous integration (CI) pipelines. NBTest offers a library of assertion APIs, and a JupyterLab plugin that enables executing assertions. We also develop the first automated approach for generating cell-level assertions for key components in ML notebooks, such as data processing, model building, and model evaluation. NBTest aims to improve the reliability and maintainability of ML notebooks without adding developer burden.
  We evaluate NBTest on 592 Kaggle notebooks. Overall, NBTest generates 21163 assertions (35.75 on average per notebook). The generated assertions obtain a mutation score of 0.57 in killing ML-specific mutations. NBTest can catch regression bugs in previous versions of the Kaggle notebooks using assertions generated for the latest versions. Because ML pipelines involve non deterministic computations, the assertions can be flaky. Hence, we also show how NBTest leverages statistical techniques to minimize flakiness while retaining high fault-detection effectiveness. NBTest has been adopted in the CI of a popular ML library. Further, we perform a user study with 17 participants that shows that notebook users find NBTest intuitive (Rating 4.3/5) and useful in writing assertions and testing notebooks (Rating 4.24/5).

## 🔍 Abstract (한글 번역)

arXiv:2509.13656v1 발표 유형: 새로운
요약: 노트북은 데이터 과학자와 기계 학습 엔지니어들이 기계 학습 (ML) 파이프라인의 프로토타이핑 및 실험에 선택한 표준 도구가 되었습니다. 노트북은 코드, 데이터 및 시각화를 위한 대화식 인터페이스를 제공합니다. 그러나 노트북은 테스트를 위한 매우 제한적인 지원만 제공합니다. 따라서 지속적인 개발 중에는 종종 충돌로 이어지지 않는 많은 섬세한 버그들이 눈에 띄지 않고 성능 회귀로 나타나는 조용한 오류를 일으킵니다.
이를 해결하기 위해, 우리는 NBTest를 소개합니다 - 개발자가 노트북에 셀 수준의 어설션을 작성하고 이러한 노트북을 pytest 또는 지속적 통합 (CI) 파이프라인에서 실행할 수 있는 최초의 회귀 테스트 프레임워크입니다. NBTest는 어설션 API 라이브러리와 어설션 실행을 가능하게 하는 JupyterLab 플러그인을 제공합니다. 또한, 데이터 처리, 모델 구축 및 모델 평가와 같은 ML 노트북의 주요 구성 요소에 대한 셀 수준 어설션을 생성하는 최초의 자동화된 접근 방식을 개발합니다. NBTest는 개발자 부담을 더하지 않고 ML 노트북의 신뢰성과 유지 관리성을 향상시키기 위해 목표를 두고 있습니다.
우리는 592개의 캐글 노트북에서 NBTest를 평가했습니다. 전체적으로, NBTest는 21163개의 어설션을 생성했으며 (노트북당 평균 35.75개), ML 특정 변이를 제거하는 뮤테이션 점수 0.57을 얻었습니다. NBTest는 최신 버전을 위해 생성된 어설션을 사용하여 이전 버전의 캐글 노트북에서 회귀 버그를 잡을 수 있습니다. ML 파이프라인은 비결정적 계산을 포함하기 때문에 어설션은 부정확할 수 있습니다. 따라서, NBTest가 어설션의 플래키를 최소화하면서 높은 결함 감지 효과를 유지하는 방법도 보여줍니다. NBTest는 인기있는 ML 라이브러리의 CI에서 채택되었습니다. 또한, 우리는 17명의 참가자와 함께 사용자 연구를 수행하여 노트북 사용자들이 NBTest를 직관적으로 (평점 4.3/5) 이해하고 어설션 작성 및 노트북 테스트에 유용하다고 평가했습니다 (평점 4.24/5).

## 📝 요약

NBTest는 머신러닝 노트북의 신뢰성과 유지보수성을 향상시키는 첫 번째 회귀 테스트 프레임워크로, 노트북에서 셀 수준의 어설션을 작성하고 pytest나 지속적 통합(CI) 파이프라인에서 실행할 수 있도록 합니다. NBTest는 어설션 API 라이브러리와 JupyterLab 플러그인을 제공하며, 데이터 처리, 모델 구축 및 모델 평가와 같은 ML 노트북의 주요 구성 요소에 대한 셀 수준의 어설션을 자동으로 생성하는 최초의 방법론을 개발합니다. NBTest는 Kaggle 노트북 592개를 평가하여 평균 35.75개의 어설션을 생성하며, ML 특정 변이를 제거하는 데 0.57의 변이 점수를 얻습니다. NBTest는 인기 있는 ML 라이브러리의 CI에서 채택되었으며, 사용자 연구에서 노트북 사용자들이 NBTest를 직관적이고 유용하게 여기는 결과를 얻었습니다.

## 🎯 주요 포인트

- 1. 노트북은 데이터 과학자와 머신 러닝 엔지니어들 사이에서 프로토타이핑과 실험에 많이 사용되고 있으며, 테스트에 대한 지원이 매우 제한적이다.

- 2. NBTest는 노트북에서 셀 수준의 어설션을 작성하고 pytest나 CI 파이프라인에서 실행할 수 있는 첫 번째 회귀 테스트 프레임워크를 소개한다.

- 3. NBTest는 ML 노트북의 핵심 구성 요소에 대한 셀 수준의 어설션을 자동으로 생성하는 첫 번째 자동화된 접근 방식을 개발하였다.

- 4. NBTest는 ML 노트북의 이전 버전에서 발생한 회귀 버그를 최신 버전을 위해 생성된 어설션을 사용하여 잡아낼 수 있다.

- 5. NBTest는 통계 기법을 활용하여 어설션의 불안정성을 최소화하고 높은 결함 감지 효과를 유지하는 방법을 보여준다.

---

*Generated on 2025-09-18 17:22:34*
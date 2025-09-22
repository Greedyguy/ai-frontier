# Neural Networks for Learnable and Scalable Influence Estimation of Instruction Fine-Tuning Data

**Korean Title:** 신경망을 통한 학습 가능하고 확장 가능한 영향 추정: 지시 세부 조정 데이터

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Efficient Instruction Fine-Tuning

## 🔗 유사한 논문
- [[2025-09-22/Toward Efficient Influence Function_ Dropout as a Compression Tool_20250922|Toward Efficient Influence Function Dropout as a Compression Tool]] (83.8% similar)
- [[2025-09-18/Pre-training under infinite compute_20250918|Pre-training under infinite compute]] (80.3% similar)
- [[2025-09-18/MetaSel_ A Test Selection Approach for Fine-tuned DNN Models_20250918|MetaSel A Test Selection Approach for Fine-tuned DNN Models]] (80.0% similar)
- [[2025-09-17/Teaching According to Talents! Instruction Tuning LLMs with Competence-Aware Curriculum Learning_20250917|Teaching According to Talents! Instruction Tuning LLMs with Competence-Aware Curriculum Learning]] (79.9% similar)
- [[2025-09-18/TICL_ Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models_20250918|TICL Text-Embedding KNN For Speech In-Context Learning Unlocks Speech Recognition Abilities of Large Multimodal Models]] (79.9% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2502.09969v3 Announce Type: replace-cross 
Abstract: Influence functions provide crucial insights into model training, but existing methods suffer from large computational costs and limited generalization. Particularly, recent works have proposed various metrics and algorithms to calculate the influence of data using language models, which do not scale well with large models and datasets. This is because of the expensive forward and backward passes required for computation, substantial memory requirements to store large models, and poor generalization of influence estimates to new data. In this paper, we explore the use of small neural networks -- which we refer to as the InfluenceNetwork -- to estimate influence values, achieving up to 99% cost reduction. Our evaluation demonstrates that influence values can be estimated with models just 0.0027% the size of full language models (we use 7B and 8B versions). We apply our algorithm of estimating influence values (called NN-CIFT: Neural Networks for effiCient Instruction Fine-Tuning) to the downstream task of subset selection for general instruction fine-tuning. In our study, we include four state-of-the-art influence functions and show no compromise in performance, despite large speedups, between NN-CIFT and the original influence functions. We provide an in-depth hyperparameter analyses of NN-CIFT. The code for our method can be found here: https://github.com/agarwalishika/NN-CIFT.

## 🔍 Abstract (한글 번역)

arXiv:2502.09969v3 발표 유형: 교차 대체  
초록: 영향 함수는 모델 학습에 중요한 통찰력을 제공하지만, 기존 방법들은 큰 계산 비용과 제한된 일반화 문제를 겪고 있습니다. 특히, 최근 연구들은 언어 모델을 사용하여 데이터의 영향을 계산하기 위한 다양한 지표와 알고리즘을 제안했지만, 이는 대규모 모델과 데이터셋에 잘 확장되지 않습니다. 이는 계산을 위한 고비용의 순방향 및 역방향 전파, 대규모 모델을 저장하기 위한 상당한 메모리 요구 사항, 새로운 데이터에 대한 영향 추정의 낮은 일반화 때문입니다. 본 논문에서는 영향 값을 추정하기 위해 '영향 네트워크(InfluenceNetwork)'라고 부르는 소형 신경망의 사용을 탐구하여 최대 99%의 비용 절감을 달성합니다. 우리의 평가에 따르면, 영향 값은 전체 언어 모델 크기의 단 0.0027%에 불과한 모델로도 추정할 수 있습니다(우리는 7B 및 8B 버전을 사용합니다). 우리는 일반적인 지시 세부 조정을 위한 하위 집합 선택이라는 다운스트림 작업에 영향 값 추정 알고리즘(NN-CIFT: Neural Networks for effiCient Instruction Fine-Tuning)을 적용합니다. 우리의 연구에서는 네 가지 최첨단 영향 함수를 포함하며, NN-CIFT와 원래의 영향 함수 간에 큰 속도 향상에도 불구하고 성능에 타협이 없음을 보여줍니다. 우리는 NN-CIFT의 하이퍼파라미터에 대한 심층 분석을 제공합니다. 우리의 방법에 대한 코드는 다음에서 찾을 수 있습니다: https://github.com/agarwalishika/NN-CIFT.

## 📝 요약

이 논문은 대규모 언어 모델에서 데이터의 영향력을 효율적으로 추정하기 위해 작은 신경망인 InfluenceNetwork를 사용하는 방법을 제안합니다. 기존 방법들은 계산 비용이 크고 일반화가 제한적이었으나, 제안된 방법은 최대 99%의 비용 절감을 달성합니다. 7B 및 8B 모델 크기의 0.0027%에 불과한 모델로도 영향력을 정확히 추정할 수 있음을 보여주며, NN-CIFT 알고리즘을 통해 일반적인 지시 미세 조정을 위한 부분 집합 선택 작업에 적용했습니다. 네 가지 최신 영향 함수와 비교해 성능 저하 없이 속도를 크게 향상시켰으며, NN-CIFT의 하이퍼파라미터 분석도 제공합니다.

## 🎯 주요 포인트

- 1. 기존의 영향 함수 계산 방법은 큰 계산 비용과 일반화의 한계를 가지고 있다.

- 2. InfluenceNetwork라는 작은 신경망을 사용하여 영향 값을 추정함으로써 최대 99%의 비용 절감을 달성했다.

- 3. 전체 언어 모델의 0.0027% 크기인 모델로도 영향 값을 정확하게 추정할 수 있다.

- 4. NN-CIFT 알고리즘을 사용하여 일반적인 지시 세부 조정의 하위 집합 선택 작업에 적용했으며 성능 저하 없이 속도를 크게 향상시켰다.

- 5. NN-CIFT의 하이퍼파라미터에 대한 심층 분석을 제공하며, 관련 코드는 GitHub에서 제공된다.

---

*Generated on 2025-09-22 14:42:57*
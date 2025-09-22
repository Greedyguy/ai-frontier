
# PhenoGnet: A Graph-Based Contrastive Learning Framework for Disease Similarity Prediction

**Korean Title:** PhenoGnet: 질병 유사성 예측을 위한 그래프 기반 대조 학습 프레임워크

## 📋 메타데이터

**Links**: [[daily/2025-09-17|2025-09-17]] [[authors/Ranga Baminiwatte|Ranga Baminiwatte]] [[authors/Kazi Jewel Rana|Kazi Jewel Rana]] [[authors/Aaron J. Masino|Aaron J. Masino]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🔬 Broad Technical**: Graph Convolutional Networks, Graph Attention Networks

## 🔗 유사한 논문
- [[A Geometric Graph-Based Deep Learning Model for Drug-Target Affinity Prediction]] (78.7% similar)
- [[Causal Clustering for Conditional Average Treatment Effects Estimation and Subgroup Discovery]] (77.1% similar)
- [[Locally_Explaining_Prediction_Behavior_via_Gradual_Interventions_and_Measuring_Property_Gradients_20250918|Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients]] (77.1% similar)
- [[Taylor-Series_Expanded_Kolmogorov-Arnold_Network_for_Medical_Imaging_Classification_20250918|Taylor-Series Expanded Kolmogorov-Arnold Network for Medical Imaging Classification]] (76.3% similar)
- [[Intelligent Healthcare Imaging Platform An VLM-Based Framework for Automated Medical Image Analysis and Clinical Report Generation]] (76.0% similar)

## 📋 저자 정보

**Authors:** Ranga Baminiwatte, Kazi Jewel Rana, Aaron J. Masino

## 📄 Abstract (원문)

Understanding disease similarity is critical for advancing diagnostics, drug
discovery, and personalized treatment strategies. We present PhenoGnet, a novel
graph-based contrastive learning framework designed to predict disease
similarity by integrating gene functional interaction networks with the Human
Phenotype Ontology (HPO). PhenoGnet comprises two key components: an intra-view
model that separately encodes gene and phenotype graphs using Graph
Convolutional Networks (GCNs) and Graph Attention Networks (GATs), and a cross
view model implemented as a shared weight multilayer perceptron (MLP) that
aligns gene and phenotype embeddings through contrastive learning. The model is
trained using known gene phenotype associations as positive pairs and randomly
sampled unrelated pairs as negatives. Diseases are represented by the mean
embeddings of their associated genes and/or phenotypes, and pairwise similarity
is computed via cosine similarity. Evaluation on a curated benchmark of 1,100
similar and 866 dissimilar disease pairs demonstrates strong performance, with
gene based embeddings achieving an AUCPR of 0.9012 and AUROC of 0.8764,
outperforming existing state of the art methods. Notably, PhenoGnet captures
latent biological relationships beyond direct overlap, offering a scalable and
interpretable solution for disease similarity prediction. These results
underscore its potential for enabling downstream applications in rare disease
research and precision medicine.

## 🔍 Abstract (한글 번역)

질병 유사성을 이해하는 것은 진단, 약물 발견 및 맞춤 치료 전략을 발전시키는 데 중요합니다. 우리는 유전자 기능 상호 작용 네트워크를 인간 표현형 온톨로지 (HPO)와 통합하여 질병 유사성을 예측하기 위해 설계된 혁신적인 그래프 기반 대조적 학습 프레임워크 인 PhenoGnet을 제시합니다. PhenoGnet은 두 가지 주요 구성 요소로 구성되어 있습니다. 그래프 합성곱 신경망 (GCN) 및 그래프 주의 신경망 (GAT)을 사용하여 유전자 및 표현형 그래프를 각각 인코딩하는 intra-view 모델과, 대조적 학습을 통해 유전자 및 표현형 임베딩을 정렬하는 공유 가중치 다층 퍼셉트론 (MLP)으로 구현된 cross view 모델로 구성됩니다. 이 모델은 알려진 유전자 표현형 연관을 양성 쌍으로 사용하고 관련 없는 쌍을 무작위로 샘플링하여 훈련됩니다. 질병은 관련된 유전자 및/또는 표현형의 평균 임베딩으로 표현되며, 코사인 유사성을 통해 쌍별 유사성이 계산됩니다. 1,100개의 유사하고 866개의 유사하지 않은 질병 쌍으로 구성된 정제된 벤치마크에서의 평가는 유전자 기반 임베딩이 AUCPR 0.9012 및 AUROC 0.8764를 달성하여 기존의 최첨단 방법을 능가하는 강력한 성능을 보여줍니다. 특히 PhenoGnet은 직접적인 중첩을 넘어 숨겨진 생물학적 관계를 포착하여 질병 유사성 예측을 위한 확장 가능하고 해석 가능한 솔루션을 제공합니다. 이러한 결과는 희귀 질병 연구 및 정밀 의학에서 하류 응용 프로그램을 가능하게 하는 잠재력을 강조합니다.

## 📝 요약

병리 유사성을 이해하는 것은 진단, 약물 발견 및 맞춤 치료 전략을 발전시키는 데 중요합니다. 본 연구는 유전자 기능 상호작용 네트워크와 인간 표현형 온톨로지(HPO)를 통합하여 질병 유사성을 예측하는 새로운 그래프 기반 대조 학습 프레임워크 인 PhenoGnet을 제안합니다. PhenoGnet은 GCN 및 GAT를 사용하여 유전자 및 표현형 그래프를 따로 인코딩하는 intra-view 모델과 유전자 및 표현형 임베딩을 대조 학습을 통해 정렬하는 cross-view 모델로 구성됩니다. 이 모델은 알려진 유전자 표현형 연관을 양성 쌍으로, 관련 없는 쌍을 음성으로 사용하여 훈련됩니다. PhenoGnet은 질병을 관련된 유전자 및/또는 표현형의 평균 임베딩으로 표현하고, 코사인 유사도를 통해 쌍별 유사성을 계산합니다. 1,100개의 유사 및 866개의 비유사 질병 쌍으로 구성된 벤치마크에서 강력한 성능을 보여주며, 기존 최첨단 방법을 능가하는 AUCPR 0.9012 및 AUROC 0.8764를 달성했습니다. 특히, PhenoGnet은 직접적인 중첩을 넘어 숨겨진 생물학적 관계를 포착하여, 질병 유사성 예측에 대한 확장 가능하고 해석 가능한 솔루션을 제공합니다. 이러한 결과는 희귀 질병 연구 및 정밀 의학에서 하류 응용 프로그램을 가능하게 하는 잠재력을 강조합니다.

## 🎯 주요 포인트

- 질병 유사성을 예측하기 위한 새로운 그래프 기반 대조 학습 프레임워크인 PhenoGnet을 제안한다.

- PhenoGnet은 유전자 기능 상호작용 네트워크와 인간 표현형 온톨로지(HPO)를 통합하여 질병 유사성을 예측한다.

- 모델은 알려진 유전자 표현형 연관을 사용하여 학습되며, 코사인 유사도를 통해 질병 간 유사성을 계산한다.

- PhenoGnet은 직접적인 중첩을 넘어 생물학적 관계를 포착하며, 희귀 질병 연구와 정밀 의학 분야에서 활용 가능성을 보여준다.

---

*Generated on 2025-09-18 17:04:59*
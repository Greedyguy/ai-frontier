
# Fine-tuning Vision Language Models with Graph-based Knowledge for Explainable Medical Image Analysis

**Korean Title:** 그래프 기반 지식을 활용한 시각 언어 모델의 미세 조정: 설명 가능한 의료 영상 분석

## 📋 메타데이터

**Links**: [[daily/2025-09-19|2025-09-19]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Explainable Medical Image Analysis

## 🔗 유사한 논문
- [[Intelligent Healthcare Imaging Platform An VLM-Based Framework for Automated Medical Image Analysis and Clinical Report Generation]] (82.8% similar)
- [[Locally_Explaining_Prediction_Behavior_via_Gradual_Interventions_and_Measuring_Property_Gradients_20250918|Locally Explaining Prediction Behavior via Gradual Interventions and Measuring Property Gradients]] (81.4% similar)
- [[Generative_AI_for_Misalignment-Resistant_Virtual_Staining_to_Accelerate_Histopathology_Workflows_20250918|Generative AI for Misalignment-Resistant Virtual Staining to Accelerate Histopathology Workflows]] (81.1% similar)
- [[Taylor-Series_Expanded_Kolmogorov-Arnold_Network_for_Medical_Imaging_Classification_20250918|Taylor-Series Expanded Kolmogorov-Arnold Network for Medical Imaging Classification]] (80.4% similar)
- [[Semi-MoE Mixture-of-Experts meets Semi-Supervised Histopathology Segmentation]] (80.1% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2503.09808v2 Announce Type: replace-cross 
Abstract: Accurate staging of Diabetic Retinopathy (DR) is essential for guiding timely interventions and preventing vision loss. However, current staging models are hardly interpretable, and most public datasets contain no clinical reasoning or interpretation beyond image-level labels. In this paper, we present a novel method that integrates graph representation learning with vision-language models (VLMs) to deliver explainable DR diagnosis. Our approach leverages optical coherence tomography angiography (OCTA) images by constructing biologically informed graphs that encode key retinal vascular features such as vessel morphology and spatial connectivity. A graph neural network (GNN) then performs DR staging while integrated gradients highlight critical nodes and edges and their individual features that drive the classification decisions. We collect this graph-based knowledge which attributes the model's prediction to physiological structures and their characteristics. We then transform it into textual descriptions for VLMs. We perform instruction-tuning with these textual descriptions and the corresponding image to train a student VLM. This final agent can classify the disease and explain its decision in a human interpretable way solely based on a single image input. Experimental evaluations on both proprietary and public datasets demonstrate that our method not only improves classification accuracy but also offers more clinically interpretable results. An expert study further demonstrates that our method provides more accurate diagnostic explanations and paves the way for precise localization of pathologies in OCTA images.

## 🔍 Abstract (한글 번역)

arXiv:2503.09808v2 발표 유형: 교차 교체  
초록: 당뇨병성 망막병증(DR)의 정확한 단계 구분은 적시 개입을 유도하고 시력 손실을 예방하기 위해 필수적입니다. 그러나 현재의 단계 구분 모델은 해석하기 어려우며, 대부분의 공개 데이터셋은 이미지 수준의 레이블 외에 임상적 추론이나 해석을 포함하지 않습니다. 본 논문에서는 그래프 표현 학습과 비전-언어 모델(VLMs)을 통합하여 설명 가능한 DR 진단을 제공하는 새로운 방법을 제시합니다. 우리의 접근법은 생물학적으로 정보가 포함된 그래프를 구성하여 혈관 형태 및 공간 연결성과 같은 주요 망막 혈관 특징을 인코딩함으로써 광학 코히어런스 단층촬영 혈관조영술(OCTA) 이미지를 활용합니다. 그래프 신경망(GNN)은 DR 단계 구분을 수행하며, 통합 기울기는 분류 결정에 영향을 미치는 중요한 노드와 엣지 및 그 개별 특징을 강조합니다. 우리는 모델의 예측을 생리학적 구조와 그 특성에 귀속시키는 이 그래프 기반 지식을 수집합니다. 그런 다음 이를 VLMs를 위한 텍스트 설명으로 변환합니다. 우리는 이러한 텍스트 설명과 해당 이미지를 사용하여 학생 VLM을 훈련시키기 위해 지시 조정을 수행합니다. 이 최종 에이전트는 단일 이미지 입력만으로 질병을 분류하고 인간이 해석할 수 있는 방식으로 그 결정을 설명할 수 있습니다. 독점 및 공개 데이터셋에 대한 실험적 평가 결과, 우리의 방법이 분류 정확도를 향상시킬 뿐만 아니라 임상적으로 더 해석 가능한 결과를 제공함을 보여줍니다. 전문가 연구는 또한 우리의 방법이 더 정확한 진단 설명을 제공하고 OCTA 이미지에서 병리의 정확한 위치를 지정할 수 있는 길을 열어준다는 것을 보여줍니다.

## 📝 요약

이 논문은 당뇨망막병증(DR)의 정확한 단계 구분을 위해 그래프 표현 학습과 시각-언어 모델(VLM)을 통합한 새로운 방법을 제안합니다. 이 방법은 광학 코히어런스 단층 촬영 혈관조영술(OCTA) 이미지를 활용하여 혈관 형태와 공간적 연결성을 포함한 망막 혈관의 주요 특징을 그래프로 표현합니다. 그래프 신경망(GNN)을 통해 DR 단계를 구분하며, 통합 기울기 기법으로 분류 결정에 중요한 노드와 엣지를 강조합니다. 이러한 그래프 기반 지식을 텍스트로 변환하여 VLM을 훈련하고, 최종 모델은 단일 이미지 입력만으로 질병을 분류하고 설명할 수 있습니다. 실험 결과, 이 방법은 분류 정확도를 높이고 임상적으로 해석 가능한 결과를 제공합니다. 전문가 연구에서는 이 방법이 더 정확한 진단 설명을 제공하고 OCTA 이미지에서 병변의 정확한 위치를 파악하는 데 도움을 준다고 평가되었습니다.

## 🎯 주요 포인트

- 1. 당뇨망막병증(DR)의 정확한 단계 구분을 위해 그래프 표현 학습과 시각-언어 모델(VLM)을 통합한 새로운 방법을 제안합니다.

- 2. 생물학적 정보를 반영한 그래프를 통해 망막 혈관의 형태와 공간적 연결성을 인코딩하여 DR 단계를 분류합니다.

- 3. 그래프 신경망(GNN)을 사용하여 DR 단계를 분류하고, 통합 기울기를 통해 중요한 노드와 엣지를 강조하여 분류 결정에 기여하는 특징을 설명합니다.

- 4. 실험 결과, 제안된 방법은 분류 정확도를 향상시키고, 임상적으로 해석 가능한 결과를 제공합니다.

- 5. 전문가 연구를 통해 제안된 방법이 더 정확한 진단 설명을 제공하며, OCTA 이미지에서 병변의 정확한 위치 파악에 기여함을 입증했습니다.

---

*Generated on 2025-09-19 15:12:49*
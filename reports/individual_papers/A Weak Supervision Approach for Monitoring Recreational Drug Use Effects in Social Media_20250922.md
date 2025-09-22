# A Weak Supervision Approach for Monitoring Recreational Drug Use Effects in Social Media

**Korean Title:** 약물 사용 효과 모니터링을 위한 약한 감독 접근법: 소셜 미디어에서의 사례 연구

## 📋 메타데이터

**Links**: [[daily/2025-09-22|2025-09-22]] [[categories/cs.AI|cs.AI]]

## 🏷️ 카테고리화된 키워드
**🚀 Evolved Concepts**: Real-time Pharmacovigilance

## 🔗 유사한 논문
- [[2025-09-18/A Comparative Analysis of Transformer Models in Social Bot Detection_20250918|A Comparative Analysis of Transformer Models in Social Bot Detection]] (78.2% similar)
- [[2025-09-18/An Attention-Based Denoising Framework for Personality Detection in Social Media Texts_20250918|An Attention-Based Denoising Framework for Personality Detection in Social Media Texts]] (77.5% similar)
- [[2025-09-19/SMARTER_ A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models_20250919|SMARTER A Data-efficient Framework to Improve Toxicity Detection with Explanation via Self-augmenting Large Language Models]] (77.2% similar)
- [[2025-09-22/Network-Based Detection of Autism Spectrum Disorder Using Sustainable and Non-invasive Salivary Biomarkers_20250922|Network-Based Detection of Autism Spectrum Disorder Using Sustainable and Non-invasive Salivary Biomarkers]] (76.6% similar)
- [[2025-09-19/Translate, then Detect_ Leveraging Machine Translation for Cross-Lingual Toxicity Classification_20250919|Translate, then Detect Leveraging Machine Translation for Cross-Lingual Toxicity Classification]] (76.3% similar)

## 📋 저자 정보

**Authors:** 

## 📄 Abstract (원문)

arXiv:2509.15266v1 Announce Type: new 
Abstract: Understanding the real-world effects of recreational drug use remains a critical challenge in public health and biomedical research, especially as traditional surveillance systems often underrepresent user experiences. In this study, we leverage social media (specifically Twitter) as a rich and unfiltered source of user-reported effects associated with three emerging psychoactive substances: ecstasy, GHB, and 2C-B. By combining a curated list of slang terms with biomedical concept extraction via MetaMap, we identified and weakly annotated over 92,000 tweets mentioning these substances. Each tweet was labeled with a polarity reflecting whether it reported a positive or negative effect, following an expert-guided heuristic process. We then performed descriptive and comparative analyses of the reported phenotypic outcomes across substances and trained multiple machine learning classifiers to predict polarity from tweet content, accounting for strong class imbalance using techniques such as cost-sensitive learning and synthetic oversampling. The top performance on the test set was obtained from eXtreme Gradient Boosting with cost-sensitive learning (F1 = 0.885, AUPRC = 0.934). Our findings reveal that Twitter enables the detection of substance-specific phenotypic effects, and that polarity classification models can support real-time pharmacovigilance and drug effect characterization with high accuracy.

## 🔍 Abstract (한글 번역)

arXiv:2509.15266v1 발표 유형: 신규  
초록: 레크리에이션 약물 사용의 실제 효과를 이해하는 것은 공중 보건 및 생의학 연구에서 여전히 중요한 과제입니다. 특히 전통적인 감시 시스템은 사용자 경험을 종종 과소 대표하기 때문입니다. 본 연구에서는 소셜 미디어(특히 트위터)를 활용하여 엑스터시, GHB, 2C-B라는 세 가지 신흥 향정신성 물질과 관련된 사용자 보고 효과의 풍부하고 필터링되지 않은 출처로 활용했습니다. 은어 용어의 큐레이션 목록과 MetaMap을 통한 생의학 개념 추출을 결합하여 이러한 물질을 언급하는 92,000개 이상의 트윗을 식별하고 약하게 주석을 달았습니다. 각 트윗은 전문가가 안내하는 휴리스틱 프로세스를 따라 긍정적 또는 부정적 효과를 보고했는지 여부를 반영하는 극성으로 레이블이 지정되었습니다. 그런 다음 물질 간 보고된 표현형 결과에 대한 기술적 및 비교 분석을 수행하고, 비용 민감 학습 및 합성 오버샘플링과 같은 기법을 사용하여 강한 클래스 불균형을 고려하여 트윗 콘텐츠에서 극성을 예측하기 위해 여러 기계 학습 분류기를 훈련했습니다. 테스트 세트에서 최고의 성능은 비용 민감 학습을 사용한 eXtreme Gradient Boosting에서 얻었습니다(F1 = 0.885, AUPRC = 0.934). 우리의 연구 결과는 트위터가 물질별 표현형 효과를 감지할 수 있음을 보여주며, 극성 분류 모델이 높은 정확도로 실시간 약물 감시 및 약물 효과 특성화를 지원할 수 있음을 보여줍니다.

## 📝 요약

이 연구는 소셜 미디어, 특히 트위터를 활용하여 엑스터시, GHB, 2C-B와 같은 신종 향정신성 물질의 사용자 보고 효과를 분석했습니다. 슬랭 용어와 MetaMap을 사용하여 92,000개 이상의 관련 트윗을 식별하고 긍정적 또는 부정적 효과로 분류했습니다. 다양한 기계 학습 분류기를 통해 트윗 내용에서 효과의 극성을 예측했으며, eXtreme Gradient Boosting이 가장 높은 성능을 보였습니다(F1 = 0.885, AUPRC = 0.934). 이 연구는 트위터가 약물의 구체적인 효과를 감지하는 데 유용하며, 극성 분류 모델이 실시간 약물 감시와 효과 특성화에 높은 정확도로 기여할 수 있음을 보여줍니다.

## 🎯 주요 포인트

- 1. 본 연구는 트위터 데이터를 활용하여 엑스터시, GHB, 2C-B와 같은 신종 향정신성 물질의 사용자 보고 효과를 분석했습니다.

- 2. MetaMap을 사용하여 92,000개 이상의 트윗을 약한 주석으로 분류하고, 긍정적 또는 부정적 효과를 반영하는 극성을 부여했습니다.

- 3. 트윗 내용에서 극성을 예측하기 위해 여러 머신러닝 분류기를 훈련했으며, eXtreme Gradient Boosting이 가장 높은 성능을 보였습니다.

- 4. 트위터는 물질별 특이적 표현형 효과를 감지할 수 있으며, 극성 분류 모델은 실시간 약물 감시와 효과 특성화에 높은 정확도로 기여할 수 있습니다.

---

*Generated on 2025-09-22 15:09:06*
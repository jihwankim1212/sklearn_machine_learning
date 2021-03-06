# -------------------------------------------------------------- #
# from IPython.display import display
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import mglearn
# -------------------------------------------------------------- #
# 5.2.1 간단한 그리드 서치
from IPython.core.display import display
from sklearn.svm import SVC
from sklearn.model_selection import train_test_split
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
# GridSearchCv (교차 검증을 사용한 그리드 서치)
from sklearn.model_selection import GridSearchCV
from sklearn.model_selection import ParameterGrid, StratifiedKFold
# -------------------------------------------------------------- #

# 5.2.1 간단한 그리드 서치
iris = load_iris()
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=0)
# print("훈련 세트의 크기 : {} 테스트 세트의 크기 : {}".format(X_train.shape[0], X_test.shape[0]))
# best_score = 0
# for gamma in [0.001, 0.01, 0.1, 1, 10, 100]:
#     for C in [0.001, 0.01, 0.1, 1, 10, 100]:
#         # 매개변수의 각 조합에 대해 SVC를 훈련시킵니다.
#         svm = SVC(gamma=gamma, C=C)
#         svm.fit(X_train, y_train)
#         # 테스트 세트로 SVC를 평가합니다.
#         score = svm.score(X_test, y_test)
#         # 점수가 더 높으면 매개변수와 함께 기록합니다.
#         if score > best_score:
#             best_score = score
#             best_parameters = {'C': C, 'gamma' : gamma}
# print("최고 점수 : {:.2f}".format(best_score))
# print("최적 매개변수 : {}".format(best_parameters))

# mglearn.plots.plot_threefold_split()
# plt.show()

# 데이터를 훈련+검증 세트와 테스트 세트로 분할   # 데이터 = (훈련+검증) +  테스트
# X_trainval, X_test, y_trainval, y_test = train_test_split(iris.data, iris.target, random_state=0)
# 훈련+검증 세트를 훈련세트와 검증세트로 분할    # (훈련+검증) = 훈련 + 검증
# X_train, X_vaild, y_train, y_valid = train_test_split(X_trainval, y_trainval, random_state=1)
# print("훈련 세트의 크기 : {}   검증 세트의 크기 : {}  테스트 세트의 크기 : {}\n".format(X_train.shape[0], X_vaild.shape[0], X_test.shape[0]))

# best_score = 0
# for gamma in [0.001, 0.01, 0.1, 1, 10, 100]:
#     for C in [0.001, 0.01, 0.1, 1, 10, 100]:
#         # 매개변수의 각 조합에 대해 SVC를 훈련시킵니다.
#         svm = SVC(gamma=gamma, C=C)
#         svm.fit(X_train, y_train)
#         # 검증 세트로 SVC를 평가합니다.
#         score = svm.score(X_vaild, y_valid)
#         # 점수가 더 높으면 매개변수와 함께 기록합니다.
#         if score >  best_score:
#             best_score = score
#             best_parameters = {'C' : C, 'gamma' : gamma}

# 훈련 세트와 검증 세트를 합쳐 모델을 다시 만든 후 테스트 세트를 사용해 평가합니다.
# svm = SVC(**best_parameters)
# svm.fit(X_trainval, y_trainval)   # 훈련 세트와 검증 세트를 합침
# test_score = svm.score(X_test, y_test)
# print("검증 세트에서 최고점수 {:.2f}".format(best_score))
# print("최적 매개변수 : ", best_parameters)
# print("최적 매개변수에서 테스트 세트 점수 : {:.2f}".format(test_score))

# 5.2.3 교차 검증을 사용한 그리드 서치
# best_score = 0
# for gamma in [0.001, 0.01, 0.1, 1, 10, 100]:
#     for C in [0.001, 0.01, 0.1, 1, 10, 100]:
#         # 매개변수의 각 조합에 대해 SVC를 훈련시킵니다.
#         svm = SVC(gamma=gamma, C=C)
#         # 교차 검증을 적용합니다.
#         scores = cross_val_score(svm, X_trainval, y_trainval, cv=5)
#         # 교차 검증 정확도의 평균을 계산합니다.
#         score = np.mean(scores)
#         # 점수가 더 높으면 매개변수와 함께 기록합니다.
#         if score >  best_score:
#             best_score = score
#             best_parameters = {'C' : C, 'gamma' : gamma}

# 훈련 세트와 검증 세트를 합쳐 모델을 다시 만든 후 테스트 세트를 사용해 평가합니다.
# svm = SVC(**best_parameters)
# svm.fit(X_trainval, y_trainval)   # 훈련 세트와 검증 세트를 합침
# test_score = svm.score(X_test, y_test)
# print("검증 세트에서 최고점수 {:.2f}".format(best_score))
# print("최적 매개변수 : ", best_parameters)
# print("최적 매개변수에서 테스트 세트 점수 : {:.2f}".format(test_score))

# mglearn.plots.plot_cross_val_selection()
# plt.show()
# mglearn.plots.plot_grid_search_overview()
# plt.show()

# GridSearchCv (교차 검증을 사용한 그리드 서치)
# param_grid = {'C' : [0.001, 0.01, 0.1, 1, 10, 100], 'gamma' : [0.001, 0.01, 0.1, 1, 10, 100]}
# print("매개변수 그리드 : \n{}".format(param_grid))
# grid_search = GridSearchCV(SVC(), param_grid, cv=5)
X_train, X_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=0)
# grid_search.fit(X_train, y_train)
# print("테스트 세트 점수 : {:.2f}".format(grid_search.score(X_test, y_test)))
# print("최적 매개변수       : {}".format(grid_search.best_params_))
# print("최상 교차 검증 점수 : {:.2f}".format(grid_search.best_score_))
# print("최고 성능 모델      : {}".format(grid_search.best_estimator_))

# DataFrame으로 변환합니다.
# results = pd.DataFrame(grid_search.cv_results_)
# 처음 다섯행을 출력 합니다.
# display(results.head())
# scores = np.array(results.mean_test_score).reshape(6, 6)
# 교차 검증 평균 점수 히트맵 그래프
# mglearn.tools.heatmap(scores, xlabel='gamma', xticklabels=param_grid['gamma'], ylabel='C', yticklabels=param_grid['C'], cmap='viridis')
# plt.show()

# fig, axes = plt.subplots(1, 3, figsize=(13, 5))
# param_grid_linear = {'C' : np.linspace(1, 2, 6), 'gamma' : np.linspace(1, 2, 6)}
# param_grid_one_og = {'C' : np.linspace(1, 2, 6), 'gamma' : np.logspace(-3, 2, 6)}
# param_grid_range  = {'C' : np.logspace(-3, 2, 6), 'gamma' : np.logspace(-7, -2, 6)}
# for param_grid, ax in zip([param_grid_linear, param_grid_one_og, param_grid_range], axes):
#     grid_search = GridSearchCV(SVC(), param_grid, cv=5)
#     grid_search.fit(X_train, y_train)
#     scores = grid_search.cv_results_['mean_test_score'].reshape(6, 6)
#     # 교차 검증 평균 점수 히트맵 그래프
#     scores_image = mglearn.tools.heatmap(scores, xlabel='gamma', ylabel='C', xticklabels=param_grid['gamma'], yticklabels=param_grid['C'], cmap='viridis', ax=ax)

# plt.colorbar(scores_image, ax=axes.tolist())
# plt.show()

# param_grid = [{'kernel':['rbf'], 'C': [0.001, 0.01, 0.1, 1, 10, 100], 'gamma':[0.001, 0.01, 0.1, 1, 10, 100]},
#               {'kernel':['linear'],'C':[0.001, 0.01, 0.1, 1, 10, 100]}]
# print("그리드 목록 \n{}".format(param_grid))
# grid_search = GridSearchCV(SVC(), param_grid, cv=5)
# grid_search.fit(X_train, y_train)
# print("최적 매개변수 : {}".format(grid_search.best_params_))
# print("최고 교차 검증 점수 : {:.2f}".format(grid_search.best_score_))
# result = pd.DataFrame(grid_search.cv_results_)
# display(result.T)

param_grid = {'C': [0.001, 0.01, 0.1, 1, 10, 100], 'gamma': [0.001, 0.01, 0.1, 1, 10, 100]}
scores = cross_val_score(GridSearchCV(SVC(), param_grid, cv=5), iris.data, iris.target, cv=5)
print("교차 검증 점수      :", scores)
print("교차 검증 평균 점수 :", scores.mean())

def nested_cv(X, y, inner_cv, outer_cv, Classifier, parameter_grid):
    outer_scores = []
    # outer_cv의 분할을 순회하는 for 루프
    # (split 메서드는 훈련과 테스트 세트에 해당하는 인덱스를 반환합니다.)
    for training_samples, test_samples in outer_cv.split(X, y):
        # 최적의 매개변수를 찾습니다.
        best_params = {}
        best_score = -np.inf
        # 매개변수 그리드를 순회합니다.
        for parameters in parameter_grid:
            # 안쪽 교차 검증의 점수를 기록합니다.
            cv_scores = []
            # inner_cv의 분할을 순회하는 for 루프
            for inner_train, inner_test in inner_cv.split(X[training_samples], y[training_samples]):
                # 훈련 데이터와 주어진 매개변수로 분류기를 만듭니다.
                clf = Classifier(**parameters)
                clf.fit(X[inner_train], y[inner_train])
                # 검증 세트로 평가합니다.
                score = clf.score(X[inner_test], y[inner_test])
                cv_scores.append(score)
            # 안쪽 교차 검증의 평균 점수를 계산합니다.
            mean_socre = np.mean(cv_scores)
            if mean_socre >  best_score:
                # 점수가 더 높으면 매개변수와 함께 기록합니다.
                best_score = mean_socre
                best_params = parameters
            # 바깥쪽 훈련 데이터 전체를 사용해 분류기를 만듭니다.
            clf = Classifier(**parameters)
            clf.fit(X[training_samples], y[training_samples])
            # 테스트 세트를 사용해 평가합니다.
            outer_scores.append(clf.score(X[test_samples], y[test_samples]))
        return np.array(outer_scores)

# 중첩 교차 검증
scores = nested_cv(iris.data, iris.target, StratifiedKFold(5), StratifiedKFold(5), SVC, ParameterGrid(param_grid))
print("교차 검증 점수 : {}".format(scores))

import pandas as pd
import seaborn as sns
from django.shortcuts import render, redirect
from avgapp.models import SurveyData
import matplotlib.pyplot as plt
import scipy.stats as stats

SIGNIFICANCE_LEVEL = 0.05
plt.rc('font',family='AppleGothic')

def mainFunc(request):
	if request.method == "GET":
		return render(request, 'main.html')

	elif request.method == "POST":
		try:
			SurveyData(
				job = request.POST.get('job'),
				gender = request.POST.get('gender'),
				game_time= request.POST.get('time'),
			).save()
			return redirect('/')
		except Exception as e:
			print('수정 자료 처리 오류 ', e)
			return render(request,'main.html')

def surveyFunc(request):
	return render(request, 'survey.html')

def listFunc(request):

	data_all = SurveyData.objects.all()
	data = pd.DataFrame(list(data_all.values()))
	gender_test, result_ttest =ttest()
	man_avg = gender_test.iloc[0]["game_time"]
	woman_avg = gender_test.iloc[1]["game_time"]

	result_anova, job_test = one_way_anova()
	total_time_job = job_test.groupby('job')['game_time'].sum().reset_index()

	return render(request, "list.html", {'data': data.to_html(), 'man_avg':man_avg, 'woman_avg':woman_avg, 'job_data':total_time_job, 'result_anova':result_anova,'result_ttest':result_ttest})



# 검정 1 : 성별에 따라  게임 사용시간 평균에 차이가 있는가?  <== t-test
def ttest():
	#	Hø : 성별에 따른 게임 사용 시간의 평균에는 차이가 없다.
	#	H1 : 성별에 따른 게임 사용 시간의 평균에는 차이가 있다.
	data_all = SurveyData.objects.all()
	data = pd.DataFrame(list(data_all.values()))
	ttest = data[['gender', 'game_time']].dropna()
	gen1 = ttest[ttest['gender']=='남자']
	gen2 = ttest[ttest['gender']=='여자']

	time1 = gen1['game_time']
	time2 = gen2['game_time']

	result_string = ""
	# 정규성 확인
	normality1=stats.shapiro(time1).pvalue
	normality2=stats.shapiro(time2).pvalue
	if normality1 > SIGNIFICANCE_LEVEL and normality2 > SIGNIFICANCE_LEVEL:
		#print(normality1, normality2)
		result_string += f'p-value ({normality1},{normality2}) > 0.05 이므로 귀무가설 기각 실패 즉, 검정1은 정규 분포를 따릅니다.<br>'

		# 등분산성
		# 표본 수에 따른 검정
		if len(ttest) <= 30:
			homoskedasticity = stats.levene(time1,time2).pvalue
		elif len(ttest) >30:
			homoskedasticity = stats.bartlett(time1,time2).pvalue

		if homoskedasticity > SIGNIFICANCE_LEVEL:
			result_string += f'p-value ({homoskedasticity}) > 0.05 이므로 귀무가설 기각 실패 즉, 검정1은 등분산성을 성립합니다.<br>'
			t_value, p_value_ttest = stats.ttest_ind(time1, time2, equal_var=False)
			if p_value_ttest > SIGNIFICANCE_LEVEL:
				result_string += f'p-value ({p_value_ttest}) > 0.05, 귀무가설 기각 실패. 즉, 차이가 없습니다.<br>'
			else:
				result_string += f'p-value ({p_value_ttest}) <= 0.05, 귀무가설 기각. 즉, 차이가 있습니다.<br>'
		else:
			result_string += f'p-value ({homoskedasticity}) <= 0.05 검정 1은 등분산성을 성립하지 않습니다..<br>'
			t_statistic, p_value = stats.ttest_ind(time1, time2, equal_var=False)

			if p_value > SIGNIFICANCE_LEVEL:
				result_string += f'p-value ({p_value}) > 0.05, 귀무가설 기각 실패. 즉, 차이가 없습니다.<br>'
			else:
				result_string += f'p-value ({p_value}) <= 0.05, 귀무가설 기각. 즉, 차이가 있습니다.<br>'

	# 정규성 확인 결과 정규 분포에 해당하지 않으므로 바로 검정을 진행합니다
	else:
		result_string += f'p-value ({normality1},{normality2}) <= 0.05 이므로 검정 1은 정규 분포를 따르지 않습니다. 따라서 비모수적 검정을 수행합니다.<br>'
		statistic, p_value = stats.mannwhitneyu(time1, time2)

		if p_value > SIGNIFICANCE_LEVEL:
			result_string += f'p-value ({p_value}) > 0.05, 귀무가설 기각 실패. 즉, 차이가 없습니다.<br>'
		else:
			result_string += f'p-value ({p_value}) <= 0.05 , 귀무가설 기각. 즉, 차이가 있습니다.<br>'
	avg_game_time = data.groupby('gender')['game_time'].mean().reset_index()
	return avg_game_time, result_string


# 검정 2 : 직업에 따라  게임 사용시간 평균에 차이가 있는가?
def one_way_anova():
	# Hø : 직업에 따른 게임 사용 시간의 평균에는 차이가 없다.
	# H1 : 직업에 따른 게임 사용 시간의 평균에는 차이가 있다.
	data_all = SurveyData.objects.all()
	data = pd.DataFrame(list(data_all.values()))
	one_way_anova = data[['job', 'game_time']].dropna()

	job1 = one_way_anova[one_way_anova['job']=='블루칼라']
	job2 = one_way_anova[one_way_anova['job']=='화이트칼라']
	job3 = one_way_anova[one_way_anova['job']=='학생']
	job4 = one_way_anova[one_way_anova['job']=='기타']

	time1 = job1['game_time']
	time2 = job2['game_time']
	time3 = job3['game_time']
	time4 = job4['game_time']

	# 정규성 확인
	normality1=stats.shapiro(time1).pvalue
	normality2=stats.shapiro(time2).pvalue
	normality3=stats.shapiro(time3).pvalue
	normality4=stats.shapiro(time4).pvalue

	# 결과 문자열을 저장할 변수
	result_string = ""

	if normality1 > SIGNIFICANCE_LEVEL and normality2 > SIGNIFICANCE_LEVEL and normality3 > SIGNIFICANCE_LEVEL and normality4 > SIGNIFICANCE_LEVEL:
		result_string += f'p-value ({normality1},{normality2},{normality3},{normality4}) > 0.05 이므로 귀무가설 기각 실패 즉, 검정1은 정규 분포를 따릅니다.<br>'

		# 등분산성
		# 표본 수에 따른 검정
		if len(one_way_anova) <= 30:
			homoskedasticity = stats.levene(time1, time2, time3, time4).pvalue
		elif len(one_way_anova) > 30:
			homoskedasticity = stats.bartlett(time1, time2, time3, time4).pvalue

		if homoskedasticity > SIGNIFICANCE_LEVEL:
			result_string += f'p-value ({homoskedasticity}) > 0.05 이므로 귀무가설 기각 실패 즉, 검정1은 등분산성을 성립합니다.<br>'
			f_value, p_value_anova = stats.f_oneway(time1, time2, time3, time4)
			if p_value_anova > SIGNIFICANCE_LEVEL:
				result_string += f'p-value ({p_value_anova}) > 0.05, 귀무가설 기각 실패. 즉, 차이가 없습니다.<br>'
			else:
				result_string += f'p-value ({p_value_anova}) <= 0.05, 귀무가설 기각. 즉, 차이가 있습니다.<br>'

		else:
			result_string += '검정 1은 등분산성을 성립하지 않습니다..<br>'
			f_value, p_value_anova = stats.f_oneway(time1, time2, time3, time4)

			if p_value_anova > SIGNIFICANCE_LEVEL:
				result_string += f'p-value ({p_value_anova}) > 0.05, 귀무가설 기각 실패. 즉, 차이가 없습니다.<br>'
			else:
				result_string += f'p-value ({p_value_anova}) <= 0.05, 귀무가설 기각. 즉, 차이가 있습니다.<br>'

	# 정규성 확인 결과 정규 분포에 해당하지 않으므로 바로 검정을 진행합니다
	else:
		result_string += f'p-value ({normality1},{normality2},{normality3},{normality4}) < 0.05 이므로 검정 1은 정규 분포를 따르지 않습니다. 따라서 비모수적 검정을 수행합니다.<br>'
		statistic, p_value = stats.kruskal(time1, time2, time3, time4)

		if p_value > SIGNIFICANCE_LEVEL:
			result_string += f' p-value ({p_value}) > 0.05, 귀무가설 기각 실패. 즉, 차이가 없습니다.<br>'
		else:
			result_string += f' p-value ({p_value})  <= 0.05 , 귀무가설 기각. 즉, 차이가 있습니다.<br>'

	return result_string, one_way_anova

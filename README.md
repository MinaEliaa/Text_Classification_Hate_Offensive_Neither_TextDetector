<!DOCTYPE html>
<html>
<head>
	<title>Text Classification: Hate, Offensive, or Neither</title>
</head>
<body>
	<h1>Size of Tweets of Classes (After Balancing Dataset)</h1>
	<ul>
		<li>Class 0 (Hate Speech): 11440 tweets</li>
		<li>Class 1 (Offensive Speech): 12000 tweets</li>
		<li>Class 2 (Neither): 12489 tweets</li>
	</ul>
	
	<h2>Statistics and Accuracy of SVM Model</h2>
	<ul>
		<li>Accuracy Score: 96.45%</li>
		<li>Precision Score: 96.59%</li>
		<li>Recall Score: 96.45%</li>
		<li>F1-Score: 96.41%</li>
	</ul>
	
	<h2>Confusion Matrix</h2>
	<table>
		<tr>
			<th></th>
			<th>Hate Speech</th>
			<th>Offensive Speech</th>
			<th>Neither</th>
		</tr>
		<tr>
			<th>Hate Speech</th>
			<td>Data 1A</td>
			<td>Data 2A</td>
			<td>Data 3A</td>
		</tr>
		<tr>
			<th>Offensive Speech</th>
			<td>Data 1B</td>
			<td>Data 2B</td>
			<td>Data 3B</td>
		</tr>
		<tr>
			<th>Neither</th>
			<td>Data 1C</td>
			<td>Data 2C</td>
			<td>Data 3C</td>
		</tr>
	</table>
</body>
</html>

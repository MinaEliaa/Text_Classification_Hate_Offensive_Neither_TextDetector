# Text_Classification_Hate_Offensive_Neither
<!DOCTYPE html>
<html>
<head>
	SVM Model to test tweet(text) if it 'Hate' , 'Offensive' , 'Neither' 
	and I connect this model with Flask Api to put it on Local server with Http Post request
</head>
<body>
	<h1>Size of Tweets of classes (After Balancing Dataset)</h1>
	<p><ul>
		<li>Class:0 (Hate Speech) = 11440 </li>
		<li>Class:1 (Offensive Speech) = 12000 </li>
		<li>Class:2 (neither) = 12489 </li>
		
	</ul></p>
	<h2>Stats and Accuarcy of SVM Model</h2>
	<ul>
		<li>Accuracy Score: -> 96.45%</li>
		<li>pre Score: -> 96.59%</li>
		<li>recall Score: -> 96.45</li>
		<li>f1-score: -> 96.41%</li>
		
		
	</ul>
	<h2>Confusion Matrix</h2>
	<ul>
		<table>
	<tr>
		<th>Label 1</th>
		<th>Label 2</th>
		<th>Label 3</th>
	</tr>
	<tr>
		<td>Data 1A</td>
		<td>Data 2A</td>
		<td>Data 3A</td>
	</tr>
	<tr>
		<td>Data 1B</td>
		<td>Data 2B</td>
		<td>Data 3B</td>
	</tr>
	<tr>
		<td>Data 1C</td>
		<td>Data 2C</td>
		<td>Data 3C</td>
	</tr>
</table>

	</ul>
</body>
</html>

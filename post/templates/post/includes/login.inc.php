 <?php


 session_start();

if(isset($_POST['submit'])){

	include 'dbh.inc.php';
	$uid = mysqli_real_escape_string($conn,$_POST['uid'] );
	$pwd = mysqli_real_escape_string($conn,$_POST['pwd'] );
	if(empty($uid) || empty($pwd)){
		header("Location: ../1.php?login=error4");
		exit(); 

	}else{
		$sql = "select * from users where user_uid = '$uid' or user_email = '$uid'";
		$result = mysqli_query($conn, $sql);
		$resultCheck = mysqli_num_rows($result);
		if($resultCheck < 1){
			header("Location: ../1.php?login=error3");
	  		exit(); 

		}else{
			if($row = mysqli_fetch_assoc($result)){

				$a = $row['user_pwd'];
       


			 	if(password_verify($pwd, $a)){
				 	$_SESSION['u_id'] = $row['user_id'];
				 	$_SESSION['u_name'] = $row['user_name'];
				 	$_SESSION['u_email'] = $row['user_email'];
				 	$_SESSION['u_uid '] = $row['user_uid'];
				 	header("Location: ../1.php?login=success");
	  		 		exit();

				 }else{
				 	$a = $row['user_pwd'];
				 	header("Location: ../1.php?login=$pwd+$a");
	  		 		exit();


				 }
			}
		}
	}






}else{
	header("Location: ../1.php?login=$pwd+$a");
	exit(); 
}













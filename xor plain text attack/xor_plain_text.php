<?php
function xor_encrypt($in, $key) {
    $key = $key;
    $text = $in;
    $outText = '';

    // Iterate through each character
    for($i=0;$i<strlen($text);$i++) {
    $outText .= $text[$i] ^ $key[$i % strlen($key)];
    }

    return $outText;
}

$c = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw%3D";
$data = array( "showpassword"=>"yes", "bgcolor"=>"#ffffff");
$shortc = "ClVLIh4ASCsCBE8lAxMacFMZV2hdVVotEhhUJQNVAmhSEV4sFxFeaAw";

$defaultdata = array( "showpassword"=>"no", "bgcolor"=>"#ffffff");
$k = xor_encrypt(json_encode($defaultdata), base64_decode($c));
# echo $k."\xA";

$tempdata = xor_encrypt(base64_decode($c), $kk);
# echo $tempdata."\xA";
# echo base64_encode(xor_encrypt(json_encode($defaultdata).'F'));
$j = json_encode($defaultdata);

echo base64_encode(xor_encrypt(json_encode($data), $kk))."\xA"; 
echo base64_encode(xor_encrypt(json_encode($defaultdata), $k));

?>
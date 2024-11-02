resource "aws_instance" "web_server" {
  ami             = "ami-07c5ecd8498c59db5"
  instance_type   = "t2.micro"
  key_name        = "7am_earth_24"
  security_groups = ["7am_earth_sep_24"]
  tags = {
    Name = "linux"
    Env  = "DEV"
  }
}

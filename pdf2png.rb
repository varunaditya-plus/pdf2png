class Pdf2png < Formula
    desc "A quick script to convert pdfs to pngs"
    homepage "https://github.com/thevarunaditya/pdf2png"
    url "https://github.com/thevarunaditya/pdf2png/archive/refs/tags/0.1.0.tar.gz"
    sha256 "ded7f214efc1c6cefb370d7e827e6bc9cb4f9e492f6c645d98e62fd15e055700"
    license "MIT"
  
    def install
      bin.install "pdf2png.sh" => "pdf2png"
      libexec.install "app.py"
    end
  
    test do
      system "#{bin}/pdf2png"
    end
  end
  
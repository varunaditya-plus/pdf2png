class Pdf2png < Formula
  desc "A quick script to convert PDFs to PNGs"
  homepage "https://github.com/varunaditya-plus/pdf2png"
  url "https://github.com/varunaditya-plus/pdf2png/archive/refs/tags/v0.1.0.tar.gz"
  sha256 "3a7503c3141aaec617532dd8b970554916ab047fd5b1b44600714c5676a9de4e"
  license "MIT"

  depends_on "python@3.12"
  depends_on "poppler"

  include Language::Python::Virtualenv

  def install
    virtualenv_install_with_resources
  end

  test do
    system "#{bin}/pdf2png", "--help"
  end
end

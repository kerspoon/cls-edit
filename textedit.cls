
class File
  """basically here so we can save the file later"""
  func __init__ :: Str 'filename'
  pvar filename :: Str

class Buffer
  """a body of text that occupies a window"""
  func get_lines() :: List Str

class LogBuffer :: Buffer
  """a special type of buffer that only contains log messages"""
  func log :: Str 'text' -> None

class FileBuffer :: Buffer
  """a buffer that gets its data from a file"""
  pvar file :: File
  pvar data :: List Str

class Window
  """a visible section of screen space"""
  var caret    :: Point
  var size     :: Point
  var location :: Point
  pvar buffer  :: Buffer
  func render  :: None

class SyntaxClass
  """keywords and rules for moving around a buffer"""
  var cases :: Dict Str Str
  func add  :: Str 'case-name' -> Str 'regexp' 
  func find :: Str 'case-name' -> List Str 'text' -> Point 'start' -> Point  

